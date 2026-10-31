# Validación del método con los acenos

Método: B3LYP/def2-SVP con ajuste de densidad, malla DFT nivel 2, geometría de S0 optimizada con DFT.
S1, T1 y T2 con TD-DFT en la aproximación de Tamm-Dancoff (TDA), en la geometría de S0.
T1 también por ΔSCF vertical. Energías en eV, molécula aislada.
Cálculos en `datos/resultados/*.json`. Tabla completa en `datos/resultados/tabla.md`.

| molécula | S1 calc | S1 exp (cristal) | T1 TDA | T1 ΔSCF | T1 exp (cristal) | S1 − 2T1 | T2 − 2T1 |
|---|---|---|---|---|---|---|---|
| antraceno | 3.47 | — | 2.07 | 2.11 | 1.80 | −0.67 | −0.61 |
| tetraceno | 2.71 | 2.32 | 1.42 | 1.45 | 1.25 | −0.14 | −0.15 |
| pentaceno | 2.17 | 1.83 | 0.97 | 0.98 | 0.86 | +0.23 | +0.15 |

## Qué reproduce

- **Tendencia de fisión:** antraceno endotérmico (−0.67), tetraceno casi isoérgico (−0.14), pentaceno exotérmico (+0.23). El orden es el correcto.
- **T1 del pentaceno:** 0.97 eV frente a 0.86 eV en el cristal. Por debajo de 1.12 eV del silicio, como se observó.
- **T1 del tetraceno y antraceno:** sobreestimados en 0.2–0.3 eV, lo esperable al comparar molécula aislada con cristal.

## Problemas abiertos (no se ocultan)

1. **El criterio T2 > 2T1 descarta al tetraceno**, que es el material de fisión que sí funciona con silicio (Einzinger *et al.*, 2019). Con nuestro cálculo, T2 − 2T1 = −0.15 eV. Hay tres posibilidades que hay que separar:
   - el criterio está mal planteado (el bloqueo de la fusión triplete-triplete depende de más que de T2 − 2T1);
   - el T2 de TDA está mal para el tetraceno;
   - el criterio es correcto y la fusión hacia T2 no es la pérdida dominante en el cristal.
   Hasta resolverlo, `candidato` no debe usarse como filtro definitivo.
2. **Comparación con el cristal.** Las referencias experimentales son del cristal, y nuestros cálculos son de molécula aislada. Las diferencias de S1 (0.3–0.4 eV) son mayores de lo que el cristal explica por sí solo. Hace falta una referencia en fase gas o en disolución para una comparación limpia.
3. **Muestra de 3 moléculas.** Es una validación cualitativa. No basta para dar una cifra de error.

## Siguiente paso

Resolver el problema 1 antes de cribar: revisar el criterio T2 con la literatura (Smith y Michl) y recalcular con un nivel de teoría de tripletes mejor, por ejemplo ΔSCF para T2 o un funcional de rango separado.
