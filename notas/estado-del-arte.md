# Estado del arte

## El límite

Shockley y Queisser (1961) calcularon por balance detallado el máximo de una célula solar con un solo
material absorbente. Cada fotón con energía por encima del gap genera **un** par electrón-hueco y el exceso
de energía se pierde como calor. Bajo el espectro AM1.5G el máximo es **33.7 %**, con un gap de unos 1.34 eV.
El silicio, con 1.12 eV, queda algo por debajo de ese máximo.

- W. Shockley, H. J. Queisser, *J. Appl. Phys.* **32**, 510 (1961).

## Cómo romperlo: multiplicar portadores

Si un fotón de alta energía genera **dos** portadores, el límite sube. Hanna y Nozik (2006) lo calcularon con
el mismo balance detallado: **del 33.7 % al 44.4 %** para un solo gap con multiplicación de portadores.

- M. C. Hanna, A. J. Nozik, *J. Appl. Phys.* **100**, 074510 (2006). DOI 10.1063/1.2356795.

## Fisión singlete

En algunos semiconductores orgánicos, el excitón singlete S1 que crea un fotón se divide en dos excitones
triplete T1 (S1 → ¹(TT) → T1 + T1). La conservación de la energía exige aproximadamente E(S1) ≥ 2 E(T1).
Para que los tripletes no se pierdan, conviene además E(T2) > 2 E(T1), que bloquea la fusión hacia T2.

- M. B. Smith, J. Michl, "Singlet Fission", *Chem. Rev.* **110**, 6891 (2010).
- M. B. Smith, J. Michl, *Annu. Rev. Phys. Chem.* **64**, 361 (2013).

Valores en el cristal, según la fuente secundaria consultada (pendiente de contrastar con la primaria):

| | E(S1) | E(T1) | E(S1) − 2E(T1) | T1 sobre el gap del Si (1.12 eV) |
|---|---|---|---|---|
| tetraceno | 2.32 eV | ~1.25 eV | ≈ −0.18 eV (activada térmicamente) | sí |
| pentaceno | 1.83 eV | ~0.86 eV | ≈ +0.11 eV (rápida, ~100 fs) | **no** |

Esto resume el problema. El pentaceno parte sus excitones muy bien, pero sus tripletes no tienen energía
suficiente para el silicio. El tetraceno sí la tiene, pero su fisión cuesta energía y es frágil. Falta la
molécula que haga las dos cosas a la vez y además sea estable.

## La prueba de concepto con silicio

Einzinger y colaboradores (MIT, 2019) transfirieron tripletes de tetraceno a una célula de silicio a través de
una capa de oxinitruro de hafnio de solo 8 Å. El rendimiento combinado de fisión y transferencia llegó a
~133 %: más de un electrón por fotón absorbido en el tetraceno.

- M. Einzinger *et al.*, *Nature* **571**, 90 (2019). DOI 10.1038/s41586-019-1339-4.

## Cribados computacionales previos

Padula, Omar, Nematiaram y Troisi (2019) cribaron una base de datos de materiales moleculares **conocidos**
con cálculos de estados excitados calibrados contra experimento. Encontraron unos 200 candidatos, la mayoría
no identificados antes como materiales de fisión. Muchos no siguen las reglas de diseño habituales.

- D. Padula, Ö. H. Omar, T. Nematiaram, A. Troisi, *Energy Environ. Sci.* **12**, 2412 (2019).
  DOI 10.1039/C9EE01508F.

**Qué aportaría este proyecto respecto a ese trabajo:**
1. Buscar también moléculas **nuevas**, generadas por IA, no solo las que ya existen en bases de datos.
2. Imponer desde el principio el **acoplamiento al silicio** (T1 ≥ 1.12 eV) y la **estabilidad**.
3. Ser **totalmente abierto**: código, geometrías, energías y criterios, para que cualquiera reproduzca cada
   número.

## Notas de método

- TD-DFT con funcionales híbridos subestima a menudo T1 y puede sufrir inestabilidad de tripletes. La
  aproximación de Tamm-Dancoff (TDA) lo mitiga, y por eso este repositorio usa TDA para los tripletes. Una
  alternativa habitual es ΔSCF (diferencia de energías UKS triplete − RKS singlete), que también se calcula.
- Los cálculos son de molécula aislada. En el cristal, S1 baja varias décimas de eV, así que la comparación
  con experimento debe hacerse por **tendencias** a lo largo de la serie de acenos, o con datos en
  disolución.
