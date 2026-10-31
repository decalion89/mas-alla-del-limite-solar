# Predicciones selladas: tres derivados del tetraceno

Fecha de sellado: 31 de octubre de 2026, antes de cualquier cálculo de estas moléculas.

Método de comprobación: el mismo que en `notas/validacion-acenos.md`. B3LYP/def2-SVP con malla nivel 2,
geometría de S0 optimizada, TDA de 3 singletes y 3 tripletes. Energías en eV.

Referencia: tetraceno con este método, S1 = 2.71, T1 = 1.42, T2 = 2.69 (S1 − 2T1 = −0.14, T2 − 2T1 = −0.15).

## Predicciones

| molécula | SMILES | S1 esperado (rango) | T1 esperado (rango) | S1 − 2T1 (rango) | T2 − 2T1 (rango) |
|---|---|---|---|---|---|
| 5,12-dimetiltetraceno | `Cc1c2ccccc2c(C)c2cc3ccccc3cc12` | 2.65 (2.55–2.75) | 1.40 (1.35–1.45) | −0.15 (−0.30–0.00) | −0.15 (−0.25–−0.05) |
| 2,3-difluorotetraceno | `Fc1cc2cc3cc4ccccc4cc3cc2cc1F` | 2.70 (2.60–2.80) | 1.42 (1.37–1.47) | −0.14 (−0.25–−0.02) | −0.15 (−0.25–−0.05) |
| 2-azatetraceno | `c1ccc2cc3cc4ncccc4cc3cc2c1` | 2.55 (2.40–2.70) | 1.32 (1.22–1.40) | −0.10 (−0.25–+0.05) | −0.10 (−0.25–+0.05) |

## Razonamiento

- **Dimetil.** Los grupos alquilo donan densidad electrónica y elevan ligeramente el orbital ocupado. Espero un
  desplazamiento pequeño al rojo de S1 y un T1 casi igual al del tetraceno.
- **Difluoro.** El flúor atrae densidad electrónica por inducción y apenas cambia las energías de excitación. Espero
  valores casi iguales a los del tetraceno.
- **Aza.** El nitrógeno en el anillo baja el orbital vacío y suele bajar S1 y T1 a la vez. Es la única de las tres
  que puede acercar la fisión al equilibrio con el silicio, pero también la que puede bajar T1 por debajo de
  1.12 eV.

Las magnitudes son estimaciones de química orgánica, no cálculos. Su valor está en medir cuánto aciertan.

## Regla de falsación

Una predicción queda refutada si **cualquiera** de sus cuatro valores queda fuera de su rango. No se ajustarán rangos
después de ver los números. Si el método se desvía de forma sistemática, lo diremos así, sin reinterpretar la
predicción.

Antes de afirmar que una de estas moléculas es nueva, buscaremos en la literatura. Un resultado "nuevo" que ya
estaba publicado no cuenta como descubrimiento.
