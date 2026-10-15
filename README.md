# cptq-promocion

Datos, código y fuentes de la pieza **"Quintana Roo ejerció 1,269.9 millones en
promoción en 2025, su máximo, y la afluencia cayó"** del Riviera Maya Economic Pulse
(publicada el 25-jul-2026 como "Más pesos, menos pasajeros").

Enlace: https://rivieramayapulse.com/analisis/mas-pesos-menos-pasajeros/

## La pregunta

¿La Riviera necesita "más presupuesto de promoción", como pide el sector? El gasto
de promoción que Quintana Roo ejerció en 2025 fue el más alto de su historia y la
afluencia cayó de todos modos. Y medido por llegada internacional, Quintana Roo
destinó a promoción en 2025 más que República Dominicana, en el presupuesto y en el
gasto.

> **Corrección del 14-oct-2026.** Este repositorio comparaba al principio el
> aprobado del Consejo con el Fondo Mixto dominicano (fuente específica 1970 de la
> Ley de Presupuesto), que es un ingreso estimado y no lo que el Ministerio de
> Turismo presupuesta para gastar en promoción. Esa comparación se retiró. El
> benchmark usa ahora el gasto de la actividad «Promoción Turística Internacional»
> del Ministerio de Turismo, aprobado y ejercido. Ver la nota de corrección en la
> pieza.

## Las dos series del CPTQ: NO se empalman

El Consejo de Promoción Turística de Quintana Roo tiene **dos cifras distintas**
por año, y mezclarlas es el error más común:

- **Aprobado** (`data/cptq_aprobado.csv`): lo que el Presupuesto de Egresos
  autorizó en diciembre. Es una intención de gasto.
- **Ejercido / devengado** (`data/cptq_ejercido.csv`): lo que realmente se gastó,
  columna Devengado del Estado Analítico del Ejercicio del Presupuesto de Egresos
  (EAEPE), renglón "Total del Gasto", de las Cuentas Públicas del propio Consejo.

Divergen fuerte por ampliaciones y subejercicios: en 2025 el aprobado fue 752.9 M
y el ejercido 1,269.9 M; en 2021 el modificado llegó a 1,485.6 M y se ejercieron
575.5 M. **Cada análisis debe declarar cuál usa. No sumar ni comparar una serie
con la otra.** La serie que cuenta la historia del gasto real es la ejercida.

Nota: el aprobado 2022 va como `n/d` (la columna Aprobado de la Cuenta Pública
2022 no se leyó con confianza; no se afirma un número que no se pudo verificar).

## El gráfico firma y la afluencia

`assets/g1_serie_afluencia.*` cruza el gasto ejercido (barras) con la afluencia
de turistas (línea). **Son dos universos distintos y no se restan:** uno son
pesos, el otro son personas. Además, la afluencia de SEDETUR tiene dos caveats
heredados de la fuente: (1) SEDETUR revisa cifras hacia atrás, así que los saltos
interanuales son indicativos, no exactos; (2) los reportes 2022+ amplían el
universo de conteo ("otros tipos de hospedaje"), por lo que 2022-2025 puede no
estar en la misma base que 2018-2021. La línea se lee como tendencia, no como
serie de precisión.

## El benchmark por llegada

`data/por_llegada_2025.csv` compara promoción por llegada internacional en 2025,
**aprobado con aprobado y ejercido con ejercido**:

| | Aprobado | Ejercido |
|---|---|---|
| República Dominicana (Promoción Turística Internacional, MITUR) | US$1.55 | US$2.70 |
| Quintana Roo (CPTQ) | US$3.81 | US$6.42 |

Tipo de cambio: promedio 2025 del **FIX del Banco de México, 19.1996 MXN/USD**
(251 observaciones) y promedio anual de la **tasa de referencia del Banco Central
de la República Dominicana, 61.9949 DOP/USD** (venta). Las llegadas de Quintana Roo
son **derivadas** (AFAC/ASUR, internacional bidireccional ÷ 2); las de RD son
conteo real del BCRD (no residentes, vía aérea).

## Contenido

```
data/
  cptq_ejercido.csv     Serie ejercida (devengado) 2018-2025, con fuente y URL por fila.
  cptq_aprobado.csv     Serie aprobada 2018-2026, con fuente y URL por fila (2022 = n/d).
  afluencia_qroo.csv    Afluencia total de turistas 2018-2025 (SEDETUR), con caveats.
  por_llegada_2025.csv  Benchmark RD vs QRoo por llegada (aprobado y ejercido, 4 filas).
chart/
  g1_serie_afluencia.py Gráfico firma (barras ejercido + línea afluencia).
  g2_por_llegada.py     Benchmark por llegada (barras, dos pares: aprobado y ejercido).
assets/
  g1_*, g2_*            PNG 800/1600 y SVG, los mismos que sirve la pieza.
  pulse-og-gasto-record.jpg  Imagen social de la pieza. Desde el 15-oct-2026 sale del
                        generador de imágenes del sitio, no de este repositorio.
```

## Fuentes

- **Ejercido y aprobado CPTQ:** Cuentas Públicas del CPTQ, SEFIPLAN Quintana Roo,
  portal `sefiplan.qroo.gob.mx/sistemas/Cpublica/`. PDFs originales públicos; el
  repositorio enlaza a la fuente en lugar de rehospedarla.
- **Aprobado 2025/2026:** Presupuesto de Egresos, Congreso de Quintana Roo
  (Decretos 313 y 198), `documentos.congresoqroo.gob.mx`.
- **Afluencia:** SEDETUR Quintana Roo, reportes "¿Cómo Vamos?".
- **Gasto de promoción RD:** Dirección General de Presupuesto (DIGEPRES), libro de
  ejecución presupuestaria 2025, capítulo 0213 Ministerio de Turismo, programa 11,
  actividad «Promoción Turística Internacional» (presupuesto inicial y devengado).
  **Llegadas RD:** Banco Central de la República Dominicana.
- **Llegadas QRoo:** AFAC (Estadística Operacional de Aeropuertos) y ASUR.
- **Tipo de cambio:** Banco de México (FIX) y Banco Central de la República
  Dominicana (tasa de referencia del mercado spot), promedios 2025.

## Reproducir

```
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python chart/g1_serie_afluencia.py
python chart/g2_por_llegada.py
```

Los PNG salen idénticos a los publicados. El SVG cambia en cada corrida solo en los
identificadores internos que matplotlib sortea; el dibujo es el mismo.

## Licencias

- **Código** (`chart/`): MIT.
- **Datos** (`data/`) y gráficos (`assets/`): CC BY 4.0. Atribución: "Riviera Maya
  Economic Pulse, a partir de SEFIPLAN Quintana Roo, SEDETUR, DIGEPRES, BCRD, Banco de México y
  AFAC/ASUR".
