import pylab as pl
import numpy as np

eqs = []
eqs.append((r"Cara de bolas"))
eqs.append((r"El pedo fantasma... una oda a la zunga..."))
eqs.append((r"Cara de Verga Mclein!"))
eqs.append((r"Tu vieja en tanga!"))
eqs.append((r"Otra puteada que no se me ocurre ahora..."))

pl.axes([0.025, 0.025, 0.95, 0.95])

for i in range(24):
    index = np.random.randint(0, len(eqs))
    eq = eqs[index]
    size = np.random.uniform(12, 32)
    x, y = np.random.uniform(0, 1, 2)
    alpha = np.random.uniform(0.25, 0.75)
    pl.text(
        x,
        y,
        eq,
        ha="center",
        va="center",
        color="#11557c",
        alpha=alpha,
        transform=pl.gca().transAxes,
        fontsize=size,
        clip_on=True,
    )
pl.xticks(())
pl.yticks(())

pl.show()
