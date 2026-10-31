"""Calcula S1, T1 y T2 de los candidatos de predicciones/2026-10-31-candidatos.md.

Mismo método que calcular_acenos.py. Uso: python scripts/calcular_candidatos.py
"""

import json
import logging
import sys
import time
import warnings
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))
warnings.filterwarnings("ignore", message="Since PySCF-2.3")

from fision.cuantica import niveles  # noqa: E402

CANDIDATOS = {
    "dimetiltetraceno": "Cc1c2ccccc2c(C)c2cc3ccccc3cc12",
    "difluorotetraceno": "Fc1cc2cc3cc4ccccc4cc3cc2cc1F",
    "azatetraceno": "c1ccc2cc3cc4ncccc4cc3cc2c1",
}
SALIDA = RAIZ / "datos" / "resultados"

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%H:%M:%S")
    for nombre, smiles in CANDIDATOS.items():
        t0 = time.time()
        logging.info(nombre)
        r = {"nombre": nombre, **niveles(smiles)}
        r["segundos"] = round(time.time() - t0)
        (SALIDA / f"candidato_{nombre}.json").write_text(json.dumps(r, indent=2, ensure_ascii=False) + "\n")
        print(nombre, {k: v for k, v in r.items() if k.endswith("_eV")}, f"{r['segundos']} s", flush=True)
