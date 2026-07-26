import csv
from style import *
ej={};af={}
for r in csv.DictReader(open("data/cptq_ejercido.csv")): ej[int(r["anio"])]=int(r["gasto_ejercido_pesos"])/1e6
for r in csv.DictReader(open("data/afluencia_qroo.csv")): af[int(r["anio"])]=int(r["turistas_caribe_mexicano"])/1e6
yrs=list(range(2018,2026))
fig,ax=base(11,6.4)
fig.subplots_adjust(bottom=0.18,top=0.9)
bars=ax.bar(yrs,[ej[y] for y in yrs],width=0.62,color=TEAL,zorder=3,label="Gasto ejercido CPTQ")
ax.bar_label(bars,labels=[f"{ej[y]:,.0f}" for y in yrs],padding=3,fontsize=9.5,color=INK)
ax.set_ylabel("Gasto de promoción ejercido (millones de pesos)",color=TEAL,fontsize=11)
ax.set_ylim(0,1450); ax.spines[["top","right"]].set_visible(False); ax.tick_params(axis="y",labelcolor=TEAL)
ax.axvline(2021.5,color=MUTED,lw=1.1,ls=(0,(5,4)),zorder=2)
ax2=ax.twinx()
ax2.plot(yrs,[af[y] for y in yrs],color=AMBER,lw=2.4,marker="o",ms=5,zorder=4,label="Afluencia (turistas)")
ax2.set_ylabel("Afluencia total de turistas (millones)",color=AMBER,fontsize=11)
ax2.set_ylim(0,24); ax2.tick_params(axis="y",labelcolor=AMBER)
ax2.spines[["top"]].set_visible(False); ax2.spines["right"].set_color(AMBER)
ax2.annotate("posible cambio de universo\nde conteo (afluencia)",xy=(2021.55,3.2),fontsize=8,color=MUTED,ha="center")
ax.set_xticks(yrs)
ax.set_title("Más pesos, menos pasajeros: gasto de promoción (barras) vs afluencia (línea), Quintana Roo 2018-2025",
             fontsize=12.5,color=INK,loc="left",pad=14,weight="bold")
fig.text(0.012,0.02,"Dos universos distintos, no se restan: barras en pesos ejercidos (Cuentas Públicas CPTQ), línea en turistas (SEDETUR).\n"
         "La afluencia 2022+ puede no estar en la misma base que 2018-2021. Riviera Maya Economic Pulse.",
         fontsize=8.2,color=MUTED,ha="left")
savemulti(fig,"g1_serie_afluencia"); print("g1 ok")
