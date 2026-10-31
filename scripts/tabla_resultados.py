"""Tabla en Markdown de los niveles calculados, comparados con experimento y evaluados con los criterios."""

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))

from fision.criterios import Niveles, evaluar  # noqa: E402

EXP = json.loads((RAIZ / "datos" / "referencias_experimentales.json").read_text())


def f(x):
    return "—" if x is None else f"{x:.2f}"


def si_no(x):
    return "—" if x is None else ("sí" if x else "no")


filas = [
    "| molécula | S1 calc | S1 exp | T1 TDA | T1 ΔSCF vert. | T1 ΔSCF adiab. | T1 exp | T2 TDA "
    "| S1 − 2T1 (calc) | T2 − 2T1 | T1 ≥ 1.12 eV | ¿candidato? |",
    "|---|---|---|---|---|---|---|---|---|---|---|---|",
]
for nombre in ("antraceno", "tetraceno", "pentaceno"):
    p = RAIZ / "datos" / "resultados" / f"{nombre}.json"
    if not p.exists():
        continue
    r = json.loads(p.read_text())
    t1 = r["t1_adiabatico_dscf_eV"] or r["t1_vertical_dscf_eV"]
    ev = evaluar(Niveles(s1=r["s1_vertical_eV"], t1=t1, t2=r["t2_vertical_tda_eV"]))
    e = EXP.get(nombre, {})
    filas.append(
        f"| {nombre} | {f(r['s1_vertical_eV'])} | {f(e.get('s1'))} | {f(r['t1_vertical_tda_eV'])} "
        f"| {f(r['t1_vertical_dscf_eV'])} | {f(r['t1_adiabatico_dscf_eV'])} | {f(e.get('t1'))} "
        f"| {f(r['t2_vertical_tda_eV'])} | {ev['energia_fision_eV']:+.2f} | {ev['margen_t2_eV']:+.2f} "
        f"| {si_no(ev['t1_sobre_silicio'])} | {si_no(ev['candidato'])} |"
    )
print("\n".join(filas))
