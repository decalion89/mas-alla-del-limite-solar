# El criterio T2 > 2 T1

## Qué afirma

Para que un material de fisión singlete no pierda tripletes, la energía del segundo triplete debe ser al menos
el doble de la del primero: E(T2) ≥ 2 E(T1). La fuente habitual es Smith y Michl (2010), que define las condiciones
energéticas de la fisión. Fuentes secundarias (una entrada de enciclopedia y un artículo de JACS de 2025) lo
citan en esa forma, aunque no siempre con la misma desigualdad estricta o no estricta. **No hemos verificado la
redacción exacta en el artículo original.**

## Por qué importa

Dos tripletes T1 pueden fusionarse en un estado T2, en la aniquilación triplete-triplete. Si E(T2) < 2 E(T1), esa
fusión es **exotérmica**: la energía de dos tripletes pasa a un estado de menor energía y se pierde como calor, lo
que reduce el rendimiento de la fisión. Si E(T2) > 2 E(T1), la fusión a T2 es **endotérmica** y está bloqueada a
temperatura baja. Por eso el criterio se refiere a la pérdida, no a la fisión en sí.

## Lo que sabemos de tetraceno

Los datos experimentales de T2 del tetraceno no están en nuestro archivo de referencias, y no los hemos verificado.
Nuestro cálculo con B3LYP/def2-SVP y TDA da E(T2) − 2 E(T1) = −0.15 eV. Ese signo está en la zona del error del
método (los errores de T1 y S1 son de 0.2–0.4 eV), así que **el cálculo no decide si el criterio se cumple**.

El tetraceno es un material que sí funciona en silicio (Einzinger et al., 2019) con un rendimiento combinado de
~133 %. Eso indica que, si hay pérdida hacia T2, es pequeña en la práctica.

## Consecuencia para el proyecto

El criterio T2 no debe ser un filtro binario. Como está hoy en `fision/criterios.py` descarta un material que
sabemos que funciona. Propuesta:

1. Tratar E(T2) − 2 E(T1) como una **penalización continua**, no como una condición.
2. Usarla solo para comparar candidatos con el mismo método de cálculo, y no como umbral absoluto.
3. Verificar cualquier candidato con un método de mayor nivel antes de tomar decisiones con su signo.

Hasta que esto esté hecho, el campo `candidato` de `evaluar()` no debe usarse para seleccionar moléculas.

## Sensibilidad al funcional (tetraceno, TDA sobre la geometría B3LYP)

| funcional | S1 | T1 | T2 | S1 − 2T1 | T2 − 2T1 |
|---|---|---|---|---|---|
| B3LYP/def2-SVP | 2.71 | 1.42 | 2.69 | −0.14 | −0.15 |
| PBE0/def2-SVP | 2.78 | 1.40 | 2.68 | −0.02 | −0.13 |

El signo de T2 − 2T1 es negativo con los dos funcionales, y su valor se mueve poco (−0.13 a −0.15 eV). Eso
indica que el resultado no es un artefacto de un funcional concreto: con TDA, el tetraceno queda ligeramente por
debajo del criterio T2 ≥ 2T1. Un funcional de rango separado (wB97X) no pudo completarse en este equipo.

Esto no prueba que la pérdida sea grande. Un −0.13 eV se traduce en pérdida pequeña en el cristal, en línea con el
rendimiento de ~133 % medido por Einzinger et al. Lo que sí queda claro es que el filtro binario `candidato` no
debe usarse para descartar moléculas.
