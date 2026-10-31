"""Niveles S1, T1 y T2 con DFT y TD-DFT (PySCF).

Método por defecto: B3LYP/def2-SVP con ajuste de densidad.
- Geometría del estado fundamental optimizada con DFT (pyberny).
- S1: TD-DFT vertical (singletes).
- T1, T2: TDA vertical (tripletes). La aproximación de Tamm-Dancoff evita
  la inestabilidad de tripletes que sufre TD-DFT completo.
- T1 adiabático por ΔSCF: energía UKS del triplete en su geometría
  relajada menos la del singlete fundamental.
"""

from rdkit import Chem
from rdkit.Chem import AllChem
from pyscf import gto, dft, tdscf
from pyscf.geomopt.berny_solver import optimize

HARTREE_EV = 27.211386245988


def geometria_inicial(smiles: str, semilla: int = 42) -> list:
    """Geometría 3D de partida con RDKit + MMFF, como lista (símbolo, xyz)."""
    m = Chem.AddHs(Chem.MolFromSmiles(smiles))
    if AllChem.EmbedMolecule(m, randomSeed=semilla) != 0:
        raise RuntimeError(f"RDKit no pudo generar geometría para {smiles}")
    AllChem.MMFFOptimizeMolecule(m)
    pos = m.GetConformer().GetPositions()
    return [(a.GetSymbol(), tuple(pos[i])) for i, a in enumerate(m.GetAtoms())]


def molecula(atomos, base: str = "def2-svp", espin: int = 0) -> gto.Mole:
    return gto.M(atom=atomos, basis=base, spin=espin, verbose=0)


def campo_medio(mol, xc: str = "b3lyp"):
    mf = (dft.UKS(mol) if mol.spin else dft.RKS(mol)).density_fit()
    mf.xc = xc
    mf.conv_tol = 1e-9
    return mf


def optimizar(mol, xc: str = "b3lyp"):
    """Optimiza la geometría y devuelve (mol optimizada, campo medio convergido)."""
    mol_opt = optimize(campo_medio(mol, xc), maxsteps=100)
    mf = campo_medio(mol_opt, xc)
    mf.kernel()
    return mol_opt, mf


def excitaciones(mf, singlete: bool, n: int = 3, tda: bool = False) -> list[float]:
    """Energías de excitación verticales en eV."""
    td = (tdscf.TDA if tda else tdscf.TDDFT)(mf)
    td.singlet = singlete
    td.nstates = n
    td.kernel()
    return [float(e) * HARTREE_EV for e in td.e]


def t1_delta_scf(mol, mf_s0, xc: str = "b3lyp", relajar: bool = True) -> float:
    """T1 por ΔSCF en eV: vertical si relajar=False, adiabático si True."""
    trip = molecula(_atomos(mol), mol.basis, espin=2)
    if relajar:
        _, mf_t = optimizar(trip, xc)
    else:
        mf_t = campo_medio(trip, xc)
        mf_t.kernel()
    return float(mf_t.e_tot - mf_s0.e_tot) * HARTREE_EV


def _atomos(mol) -> list:
    return [(mol.atom_symbol(i), tuple(c)) for i, c in enumerate(mol.atom_coords(unit="Angstrom"))]


def niveles(smiles: str, xc: str = "b3lyp", base: str = "def2-svp", relajar_t1: bool = True) -> dict:
    """Pipeline completo para una molécula."""
    mol, mf = optimizar(molecula(geometria_inicial(smiles), base), xc)
    s = excitaciones(mf, singlete=True, n=3)
    t = excitaciones(mf, singlete=False, n=3, tda=True)
    return {
        "smiles": smiles,
        "metodo": f"{xc}/{base}",
        "e_s0_hartree": float(mf.e_tot),
        "s1_vertical_eV": s[0],
        "t1_vertical_tda_eV": t[0],
        "t2_vertical_tda_eV": t[1],
        "t1_vertical_dscf_eV": t1_delta_scf(mol, mf, xc, relajar=False),
        "t1_adiabatico_dscf_eV": t1_delta_scf(mol, mf, xc, relajar=True) if relajar_t1 else None,
        "geometria_angstrom": [[s, *map(float, c)] for s, c in _atomos(mol)],
    }
