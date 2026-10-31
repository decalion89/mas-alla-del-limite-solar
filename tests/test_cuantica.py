"""Prueba rápida del pipeline cuántico con una molécula diminuta."""

import warnings

import pytest

pytest.importorskip("pyscf")
warnings.filterwarnings("ignore", message="Since PySCF-2.3")

from fision.cuantica import excitaciones, geometria_inicial, molecula, optimizar, t1_delta_scf  # noqa: E402


def test_etileno_sto3g():
    mol, mf = optimizar(molecula(geometria_inicial("C=C"), "sto-3g"))
    s = excitaciones(mf, singlete=True, n=2)
    t = excitaciones(mf, singlete=False, n=2, tda=True)
    t1 = t1_delta_scf(mol, mf, relajar=False)
    # El triplete más bajo queda por debajo del singlete (regla de Hund)
    assert 0 < t[0] < s[0]
    # TDA y ΔSCF dan T1 compatibles para el etileno
    assert abs(t1 - t[0]) < 0.3
