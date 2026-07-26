import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
INK="#0A1628"; PAPER="#F7F5F0"; TEAL="#0B5D5B"; SAND="#C9B28A"; AMBER="#A8741A"; MUT="#8296AE"
fig=plt.figure(figsize=(12,6.3),dpi=100); fig.patch.set_facecolor(INK)
ax=fig.add_axes([0,0,1,1]); ax.set_facecolor(INK); ax.axis("off"); ax.set_xlim(0,1); ax.set_ylim(0,1)
ax.plot([0.06,0.20],[0.90,0.90],color=TEAL,lw=3)
ax.text(0.06,0.845,"RIVIERA MAYA ECONOMIC PULSE  ·  ANÁLISIS",color=TEAL,fontsize=15,family="DejaVu Sans",weight="bold",va="center")
ax.text(0.06,0.60,"Gasto récord en promoción,",color=PAPER,fontsize=44,family="DejaVu Serif",weight="bold",va="center")
ax.text(0.06,0.475,"afluencia a la baja",color=PAPER,fontsize=44,family="DejaVu Serif",weight="bold",va="center")
ax.text(0.06,0.30,"Quintana Roo ejerció su gasto de promoción más alto en 2025, 2.2 veces el de 2018,",color=MUT,fontsize=15.5,family="DejaVu Sans",va="center")
ax.text(0.06,0.245,"y la afluencia cayó de todos modos. El benchmark con República Dominicana.",color=MUT,fontsize=15.5,family="DejaVu Sans",va="center")
# barritas motivo (creciente)
import numpy as np
xs=np.linspace(0.06,0.30,6); hs=[0.05,0.058,0.05,0.075,0.09,0.13]
for x,h in zip(xs,hs): ax.add_patch(plt.Rectangle((x,0.10),0.028,h,color=TEAL))
ax.text(0.94,0.10,"rivieramayapulse.com",color=SAND,fontsize=13,family="DejaVu Sans",ha="right",va="center")
fig.savefig("assets/pulse-og-gasto-record.jpg",dpi=100,facecolor=INK,bbox_inches=None)
print("og escrita")
