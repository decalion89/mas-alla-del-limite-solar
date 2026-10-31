from fision.criterios import Niveles, energia_fision, evaluar, margen_t2


def test_pentaceno_fision_exoergica_pero_triplete_bajo():
    r = evaluar(Niveles(s1=1.83, t1=0.86))
    assert r["energia_fision_eV"] == 0.11
    assert r["fision_permitida"]
    assert not r["t1_sobre_silicio"]
    assert not r["candidato"]


def test_tetraceno_es_candidato_con_tolerancia_termica():
    r = evaluar(Niveles(s1=2.32, t1=1.25))
    assert abs(energia_fision(Niveles(2.32, 1.25)) + 0.18) < 1e-12
    assert r["fision_permitida"]
    assert r["t1_sobre_silicio"]
    assert r["t2_bloqueado"] is None
    assert r["candidato"]


def test_sin_tolerancia_el_tetraceno_no_pasa():
    assert not evaluar(Niveles(2.32, 1.25), tolerancia=0.0)["fision_permitida"]


def test_t2_por_debajo_de_dos_t1_descarta():
    n = Niveles(s1=2.6, t1=1.25, t2=2.3)
    assert margen_t2(n) < 0
    assert not evaluar(n)["candidato"]
