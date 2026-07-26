import csv
from style import *
rows=list(csv.DictReader(open("data/por_llegada_2025.csv")))
labels=["Rep. Dominicana\n(presupuesto)","Quintana Roo\n(aprobado)","Quintana Roo\n(ejercido)"]
vals=[float(r["por_llegada_usd"]) for r in rows]; cols=[SAND,MUTED,TEAL]
fig,ax=base(9,6.0)
fig.subplots_adjust(bottom=0.30,top=0.9)
bars=ax.bar(labels,vals,width=0.6,color=cols,zorder=3)
ax.bar_label(bars,labels=[f"US${v:.2f}" for v in vals],padding=4,fontsize=12,color=INK,weight="bold")
ax.set_ylabel("Promoción por llegada internacional, 2025 (USD)",fontsize=11)
ax.set_ylim(0,7.4); ax.spines[["top","right"]].set_visible(False)
ax.axhline(vals[0],color=SAND,lw=1,ls=(0,(4,3)),zorder=1)
ax.set_title("Lo que cada destino gasta en promoción por visitante, 2025",fontsize=13,color=INK,loc="left",pad=12,weight="bold")
fig.text(0.012,0.015,"En el papel QRoo destina menos por llegada que Rep. Dominicana (US$3.80 vs 5.32); con el gasto ejercido de 2025,\n"
         "terminó gastando más (US$6.42). Tipo de cambio promedio 2025 = 19.21 MXN/USD (DEXMXUS, base Banxico); RD a 61.49 DOP/USD.\n"
         "Llegadas QRoo derivadas (AFAC/ASUR bidireccional/2). Riviera Maya Economic Pulse.",
         fontsize=8.2,color=MUTED,ha="left")
savemulti(fig,"g2_por_llegada"); print("g2 ok")
