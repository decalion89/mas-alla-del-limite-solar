"""Sensibilidad de S1, T1 y T2 al funcional, sobre la geometría de S0 ya optimizada.

Uso: python scripts/sensibilidad_funcional.py tetraceno wb97x pbe0

Usa la geometría de datos/resultados/<molécula>.json, así que solo recalcula la
parte electrónica: SCF del singlete y TDA de singletes y tripletes. Cada funcional
se guarda en datos/resultados/sensibilidad_<molécula>_<funcional>.json.
"""

import json
import sys
import time
import warnings
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))
warnings.filterwarnings("ignore", message="Since PySCF-2.3")

from fision.cuantica import HARTREE_EV, campo_medio, excitaciones, molecula  # noqa: E402

RESULTADOS = RAIZ / "datos" / "resultados"


def cargar_geometria(nombre: str) -> list:
    datos = json.loads((RESULTADOS / f"{nombre}.json").read_text())
    return [(s, tuple(xyz)) for s, *xyz in datos["geometria_angstrom"]]


def calcular(nombre: str, xc: str) -> dict:
    t0 = time.time()
    mol = molecula(cargar_geometria(nombre))
    mf = campo_medio(mol, xc)
    mf.kernel()
    s1 = excitaciones(mf, singlete=True, n=3)
    t = excitaciones(mf, singlete=False, n=3)
    return {
        "molecula": nombre,
        "funcional": xc,
        "metodo": f"{xc}/def2-svp, TDA, geometria B3LYP",
        "s1_tda_eV": s1,
        "t1_tda_eV": t[0],
        "t2_tda_eV": t[1],
        "s1_menos_2t1_eV": s1[0] - 2 * t[0],
        "t2_menos_2t1_eV": t[1] - 2 * t[0],
        "segundos": round(time.time() - t0),
    }


if __name__ == "__main__":
    molec, *funcionales = sys.argv[1:]
    for xc in funcionales:
        r = calcular(molec, xc)
        (RESULTADOS / f"sensibilidad_{molec}_{xc}.json").write_text(
            json.dumps(r, indent=2, ensure_ascii=False) + "\n"
        )
        print(xc, {k: v for k, v in r.items() if k.endswith("_eV")}, f"{r['segundos']} s", flush=True)
