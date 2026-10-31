"""Criterios energéticos de un buen material de fisión singlete.

Todas las energías en eV, medidas desde el estado fundamental S0.

Un material útil para sensibilizar silicio debe cumplir, a la vez:

1. Fisión exoérgica o casi isoérgica: E(S1) >= 2 E(T1) - tolerancia.
   Si E(S1) es mucho menor que 2 E(T1), el singlete no puede partirse en
   dos tripletes. Una pequeña endoergicidad (~0.2 eV, como en el tetraceno
   cristalino) puede compensarse con entropía y temperatura.
2. Sin pérdida por aniquilación triplete-triplete hacia T2:
   E(T2) > 2 E(T1). Si no, dos tripletes pueden fusionarse en T2 y
   la energía se pierde como calor.
3. Triplete por encima del gap del silicio: E(T1) >= 1.12 eV, para que
   cada triplete pueda inyectar un electrón-hueco en el silicio.
"""

from dataclasses import dataclass

GAP_SILICIO_EV = 1.12
TOLERANCIA_FISION_EV = 0.2


@dataclass(frozen=True)
class Niveles:
    s1: float
    t1: float
    t2: float | None = None


def energia_fision(n: Niveles) -> float:
    """ΔE_SF = E(S1) - 2 E(T1). Positivo: la fisión libera energía."""
    return n.s1 - 2 * n.t1


def margen_t2(n: Niveles) -> float | None:
    """E(T2) - 2 E(T1). Positivo: la fusión hacia T2 está bloqueada."""
    if n.t2 is None:
        return None
    return n.t2 - 2 * n.t1


def evaluar(n: Niveles, tolerancia: float = TOLERANCIA_FISION_EV) -> dict:
    """Comprueba los tres criterios y devuelve el detalle."""
    m2 = margen_t2(n)
    criterios = {
        "fision_permitida": energia_fision(n) >= -tolerancia,
        "t2_bloqueado": None if m2 is None else m2 > 0,
        "t1_sobre_silicio": n.t1 >= GAP_SILICIO_EV,
    }
    return {
        "energia_fision_eV": round(energia_fision(n), 3),
        "margen_t2_eV": None if m2 is None else round(m2, 3),
        **criterios,
        "candidato": all(v is not False for v in criterios.values()),
    }
