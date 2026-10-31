# Más allá del límite solar

**Sergi Galán** · proyecto de investigación abierto, 2026

[![tests](https://github.com/decalion89/mas-alla-del-limite-solar/actions/workflows/tests.yml/badge.svg)](https://github.com/decalion89/mas-alla-del-limite-solar/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Una célula solar de silicio no puede convertir en electricidad más de un tercio de la luz del Sol. Es un límite
físico, el de **Shockley y Queisser (1961)**: cada fotón genera como mucho un electrón, y la energía que le
sobra a la luz azul y verde se pierde como calor.

Hay una forma de romperlo. En algunas moléculas, un fotón de alta energía crea un excitón *singlete* (S1) que
se **divide en dos excitones *triplete*** (T1). Es la **fisión singlete**: un fotón, dos electrones. Acoplada
al silicio, sube el límite teórico **del 33.7 % al 44.4 %** (Hanna y Nozik, 2006). En 2019 un equipo del MIT
demostró que los tripletes del tetraceno pueden entrar en una célula de silicio (Einzinger *et al.*,
*Nature*).

**Lo que falta es la molécula.** Las que se conocen fallan en algo: o sus tripletes no tienen energía
suficiente para el silicio (pentaceno), o su fisión cuesta energía y son frágiles (tetraceno).

Este repositorio busca esa molécula con química cuántica e inteligencia artificial, de forma abierta y
reproducible.

## Qué buscamos

Una molécula que cumpla a la vez, con energías en eV medidas desde el estado fundamental:

| criterio | condición | por qué |
|---|---|---|
| fisión permitida | E(S1) ≥ 2 E(T1) − 0.2 | el singlete debe poder pagar dos tripletes; ~0.2 eV se compensan térmicamente |
| sin pérdidas hacia T2 | E(T2) > 2 E(T1) | si no, dos tripletes se fusionan en T2 y la energía se pierde |
| encaje con el silicio | E(T1) ≥ 1.12 eV | cada triplete debe poder inyectar carga en el silicio |
| estable | (fase 3) | que aguante luz y aire durante años |

Implementado en [`fision/criterios.py`](fision/criterios.py).

## Plan

1. **Validar el método** con los acenos conocidos (antraceno, tetraceno, pentaceno): ¿reproduce el cálculo
   las tendencias experimentales? ← *estamos aquí*
2. **Modelo de IA** entrenado con cálculos cuánticos que prediga S1, T1 y T2 en milisegundos.
3. **Cribado** de millones de moléculas conocidas y nuevas (generadas por IA), con filtros de estabilidad y de
   síntesis.
4. **Verificación** de los mejores candidatos con métodos cuánticos de mayor nivel.
5. **Publicación abierta** de los candidatos y búsqueda de un laboratorio que los sintetice y mida.

## Estructura

| ruta | contenido |
|---|---|
| [`fision/cuantica.py`](fision/cuantica.py) | DFT/TD-DFT con PySCF: geometría, S1 (TD-DFT), T1 y T2 (TDA), T1 por ΔSCF |
| [`fision/criterios.py`](fision/criterios.py) | criterios de un buen material de fisión para silicio |
| [`scripts/calcular_acenos.py`](scripts/calcular_acenos.py) | cálculo de los acenos de referencia |
| [`scripts/tabla_resultados.py`](scripts/tabla_resultados.py) | tabla comparativa con experimento |
| [`datos/`](datos/) | referencias experimentales y resultados calculados (JSON, con geometrías) |
| [`notas/estado-del-arte.md`](notas/estado-del-arte.md) | estado del arte con referencias |
| [`docs/ideas.md`](docs/ideas.md) | catálogo de ideas que se consideraron antes de elegir este proyecto |

## Reproducir

```bash
pip install -r requirements.txt
pytest -q                          # tests rápidos (< 1 min)
python scripts/calcular_acenos.py  # B3LYP/def2-SVP; decenas de minutos en 4 núcleos
python scripts/tabla_resultados.py
```

## Honestidad

- Los cálculos son de molécula aislada. Los valores experimentales de referencia son del cristal, donde S1 es
  varias décimas de eV más bajo. Comparamos tendencias, no números sueltos.
- Una molécula en el ordenador no es una molécula en el laboratorio. La validación final necesita síntesis y
  espectroscopía.
- Ya hubo un cribado de moléculas conocidas (Padula *et al.*, 2019). Lo nuevo aquí es buscar también moléculas
  generadas, exigir desde el principio el encaje con el silicio y la estabilidad, y publicarlo todo.
