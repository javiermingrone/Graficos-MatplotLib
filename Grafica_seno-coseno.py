import pylab as pl
import numpy as np

# Crear una figura de 8x6 puntos de tamaño, 80 puntos por pulgada
pl.figure(figsize=(8, 6), dpi=80)
# Crear una nueva subgráfica de 1x1
pl.subplot(1, 1, 1)
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
# En uno de los parámetros puedo especificar el color y el grosor de la línea para la gráfica en este caso elijo Rojo "Red" y Grosor 2,
# el parámetro LineStyle define el tipo de Línea. En este caso voy a elegir -. para que se diferencie con la segunda gráfica
pl.plot(X, C, color="Red", linewidth=2.0, linestyle="-.")
# Voy a cambiar de la segunda gráfica el color a Amarillo, Blue y el Grosor de la Línea a 4, tipor de línea -.
pl.plot(X, S, color="Blue", linewidth=4.0, linestyle="-")
# Puedo poner límites para el Eje x. En el punto anterior la gráfica no tenía límites en este caso va a ir de -4 a 4
pl.xlim(-4.0, 4.0)
# Ticks en x - Con xticks puedo cambiar la graduación del eje
pl.xticks(np.linspace(-4, 4, 9, endpoint=True))
# Puedo poner límites para el Eje y. En el punto anterior la gráfica no tenía límites en este caso va a ir de -1 a 1
pl.ylim(-1.0, 1.0)
# Ticks en y Con yticks puedo cambiar la graduación del eje
pl.yticks(np.linspace(-1, 1, 5, endpoint=True))

# Configuro los Spines de la siguiente manera
ax = pl.gca()
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.xaxis.set_ticks_position("bottom")
ax.spines["bottom"].set_position(("data", 0))
ax.yaxis.set_ticks_position("left")
ax.spines["left"].set_position(("data", 0))
# Puedo poner límites para el Eje x. En el punto anterior la gráfica no tenía límites en este caso va a ir de -4 a 4
pl.xlim(-4.0, 4.0)
# Ticks en x - Con xticks puedo cambiar la graduación del eje
pl.xticks(np.linspace(-4, 4, 9, endpoint=True))
# Puedo poner límites para el Eje y. En el punto anterior la gráfica no tenía límites en este caso va a ir de -1 a 1
pl.ylim(-1.0, 1.0)
# Ticks en y Con yticks puedo cambiar la graduación del eje
pl.yticks(np.linspace(-1, 1, 5, endpoint=True))

# Agrego el parámetro label para luego mostrar la leyenda
pl.plot(X, S, color="Blue", linewidth=4.0, linestyle="-", label="Función Seno")

# Anotaciones en el Gráfico.
t = 2 * np.pi / 3
# Trazo la Linea de la función coseno hasta el Eje en Color Azul
pl.plot([t, t], [0, np.cos(t)], color="blue", linewidth=1.5, linestyle="--")
# Grafico el punto Azul de la función Coseno
pl.scatter(
    [
        t,
    ],
    [
        np.cos(t),
    ],
    50,
    color="blue",
)
pl.annotate(
    r"$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$",
    xy=(t, np.sin(t)),
    xycoords="data",
    xytext=(+10, +30),
    textcoords="offset points",
    fontsize=16,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
# Trazo la Linea de la función seno hasta el Eje en Color Verde
pl.plot([t, t], [0, np.sin(t)], color="Green", linewidth=1.5, linestyle="--")
# Trazo el Punto de la función Seno en Verde
pl.scatter(
    [
        t,
    ],
    [
        np.sin(t),
    ],
    50,
    color="Green",
)
pl.annotate(
    r"$cos(\frac{2\pi}{3})=-\frac{1}{2}$",
    xy=(t, np.cos(t)),
    xycoords="data",
    xytext=(-90, -50),
    textcoords="offset points",
    fontsize=16,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
# Muestro el Resultado por Pantalla
pl.show()
