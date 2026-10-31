"""Calcula S1, T1 y T2 de los acenos de referencia y guarda un JSON por molécula.

Uso: python scripts/calcular_acenos.py [nombre ...]
"""

import json
import sys
import time
import warnings
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
warnings.filterwarnings("ignore", message="Since PySCF-2.3")

from fision.cuantica import niveles  # noqa: E402

ACENOS = {
    "antraceno": "c1ccc2cc3ccccc3cc2c1",
    "tetraceno": "c1ccc2cc3cc4ccccc4cc3cc2c1",
    "pentaceno": "c1ccc2cc3cc4cc5ccccc5cc4cc3cc2c1",
}
SALIDA = Path(__file__).resolve().parents[1] / "datos" / "resultados"

if __name__ == "__main__":
    for nombre in sys.argv[1:] or ACENOS:
        t0 = time.time()
        r = {"nombre": nombre, **niveles(ACENOS[nombre])}
        r["segundos"] = round(time.time() - t0)
        (SALIDA / f"{nombre}.json").write_text(json.dumps(r, indent=2, ensure_ascii=False) + "\n")
        print(nombre, {k: v for k, v in r.items() if k.endswith("_eV")}, f"{r['segundos']} s", flush=True)
