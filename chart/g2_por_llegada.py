"""Gráfico 2: promoción por llegada internacional, 2025, aprobado y ejercido.
Misma lógica de dibujo que datos/mas-pesos-menos-pasajeros/genera_g2.py del sitio (sellado); aquí lee
data/por_llegada_2025.csv y escribe en assets/. Las cifras son las de la corrección del 14-oct-2026:
https://rivieramayapulse.com/analisis/mas-pesos-menos-pasajeros/
Uso, desde la raíz del repo: python chart/g2_por_llegada.py
"""
import csv, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SALIDA = os.path.join(RAIZ, "assets")
v = {}
for r in csv.DictReader(open(os.path.join(RAIZ, "data", "por_llegada_2025.csv"))):
    pais = "RD" if r["moneda"] == "DOP" else "QR"
    v[(pais, "aprob" if r["etapa"] == "aprobado" else "ejerc")] = float(r["por_llegada_usd"])

TINTA, GRIS, FONDO, ARENA, TEAL = "#0a1628", "#5e6a7c", "#f7f5f0", "#c9b28a", "#0b5d5b"
plt.rcParams.update({"font.family": "DejaVu Sans", "svg.fonttype": "path"})
fig, ax = plt.subplots(figsize=(8.192, 5.86))
fig.patch.set_facecolor(FONDO); ax.set_facecolor(FONDO)
x = [0, 1]; w = 0.36
for dx, pais, color, nombre in ((-w/2, "RD", ARENA, "República Dominicana"), (w/2, "QR", TEAL, "Quintana Roo")):
    ys = [v[(pais, "aprob")], v[(pais, "ejerc")]]
    bars = ax.bar([i + dx for i in x], ys, w, color=color, label=nombre, zorder=2)
    for b, y in zip(bars, ys):
        ax.text(b.get_x() + b.get_width()/2, y + 0.12, f"US${y:.2f}", ha="center", va="bottom",
                fontsize=12, fontweight="bold", color=TINTA)
ax.set_xticks(x, ["Aprobado", "Ejercido"], fontsize=12, color=GRIS)
ax.set_ylabel("Promoción por llegada internacional, 2025 (USD)", fontsize=10.5, color=TINTA)
ax.set_ylim(0, 7.4); ax.tick_params(axis="y", colors=GRIS, labelsize=11)
for s in ("top", "right"): ax.spines[s].set_visible(False)
for s in ("left", "bottom"): ax.spines[s].set_color(TINTA)
ax.legend(frameon=False, fontsize=11, loc="upper left", labelcolor=TINTA)
fig.suptitle("Promoción por llegada internacional, 2025", x=0.14, ha="left", fontsize=13.5,
             fontweight="bold", color=TINTA)
fig.text(0.012, 0.015,
         "RD: actividad «Promoción Turística Internacional», MITUR (DIGEPRES, libro de ejecución 2025). QRoo: CPTQ\n"
         "(Presupuesto de Egresos y Cuenta Pública). Tipo de cambio promedio 2025: 19.20 MXN/USD (FIX, Banxico) y\n"
         "61.99 DOP/USD (BCRD). Llegadas QRoo derivadas (AFAC/ASUR bidireccional/2). Riviera Maya Economic Pulse.",
         fontsize=7.6, color=GRIS, va="bottom")
fig.subplots_adjust(left=0.1, right=0.98, top=0.9, bottom=0.2)
fig.savefig(os.path.join(SALIDA, "g2_por_llegada.svg"), facecolor=FONDO, metadata={"Date": None})
fig.savefig(os.path.join(SALIDA, "g2_por_llegada_1600.png"), dpi=200, facecolor=FONDO)
fig.savefig(os.path.join(SALIDA, "g2_por_llegada_800.png"), dpi=100, facecolor=FONDO)
print({k: v[k] for k in v})
