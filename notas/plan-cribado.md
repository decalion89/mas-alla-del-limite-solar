# Plan de cribado: cuánto cuesta y cómo se reduce

## Lo que hemos medido

Tiempos reales en 4 núcleos, B3LYP/def2-SVP, optimización de S0 más TDA de 3 singletes y 3 tripletes:

| molécula | átomos | funciones de base | tiempo total |
|---|---|---|---|
| antraceno | 24 | 246 | 20 min |
| tetraceno | 30 | 312 | 33 min |
| pentaceno | 36 | 378 | 74 min |

El número de funciones de base sale de la composición (def2-SVP: 14 por C, 5 por H, con funciones esféricas).
La validación de PySCF para naftaleno dio 180 funciones, que coincide.

Con estos tiempos, cribar 1 000 moléculas del tamaño del tetraceno tomaría unas 4 000 horas de cálculo en esta
máquina. No es viable, así que el cribado necesita reducir el coste de tres formas.

## Tres vías, de menos a más ambiciosa

1. **Cálculo en GPU.** GPU4PySCF implementa DFT y TDDFT en GPU con la misma API. Es la mejora más directa: suele
   dar un orden de magnitud o más en moléculas de este tamaño. Hay que comprobar que reproduce los números de
   CPU en el tetraceno antes de usarlo, con la misma tolerancia que en `notas/validacion-acenos.md`.
2. **Modelo sustituto (ML).** Entrenar un modelo con los cálculos de alto nivel para predecir S1, T1 y T2 a partir
   de la estructura. Con unos cientos de moléculas calculadas, un modelo de grafos da un error de unas décimas de
   eV, que basta para descartar lo claramente malo. Sus predicciones se confirman siempre con el cálculo completo.
3. **Cribado en dos niveles.** Filtrar primero con el modelo y calcular solo los mejores candidatos con DFT. Es lo
   que hace el proyecto en su fase 3.

## Qué no hacemos

- No usamos una base pequeña para el cribado sin calibrarla. Una base menor cambia las energías de excitación, y
  hay que medir ese cambio contra la base def2-SVP sobre un conjunto de referencia antes de usarla.
- No confiamos en el signo de T2 − 2T1 como filtro. Ver `notas/criterio-T2.md`.

## Decisión pendiente

La vía 1 cuesta dinero o acceso a GPU, que no tenemos en este contenedor. Mientras tanto, la vía 2 puede empezar con
los tres acenos y las moléculas que se calculen después.
