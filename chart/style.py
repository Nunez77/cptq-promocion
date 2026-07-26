import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
PAPER="#F7F5F0"; INK="#0A1628"; BODY="#2A3441"; MUTED="#5E6A7C"; HAIR="#DFDAD0"
TEAL="#0B5D5B"; SAND="#C9B28A"; RED="#B23A2E"; GREEN="#1F7A4C"; AMBER="#A8741A"
def base(w=11, h=6.2):
    plt.rcParams.update({
        "font.family":"DejaVu Sans","font.size":12,
        "axes.edgecolor":INK,"axes.linewidth":1.0,
        "figure.facecolor":PAPER,"axes.facecolor":PAPER,
        "text.color":BODY,"axes.labelcolor":BODY,"xtick.color":MUTED,"ytick.color":MUTED,
    })
    fig,ax=plt.subplots(figsize=(w,h),dpi=145)
    fig.patch.set_facecolor(PAPER); ax.set_facecolor(PAPER)
    return fig,ax
def savemulti(fig, stem):
    for suf,dpi in (("_1600",200),("_800",100)):
        fig.savefig(f"assets/{stem}{suf}.png",dpi=dpi,bbox_inches="tight",facecolor=PAPER)
    fig.savefig(f"assets/{stem}.svg",bbox_inches="tight",facecolor=PAPER)
