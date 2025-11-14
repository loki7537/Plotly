import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import numpy.core.function_base as core
import numpy as np

# Creating the data
r1 = 0.8  # диаметр первичной спирали
r2 = 0.45  # диаметр вторичной спирали
r3 = 0.2  # диаметр третьей спирали
r4 = 0.01

w = 30  # количество витков вторичной спирали на шаг
w2 = 500  # количество витков ТРЕТИЧНОЙ спирали на шаг

h = 0.3  # шаг первичной спирали


t = core.linspace(-3.14*2, 3.14*2, num = 50000)

"""x = a cos t,
   y = a sin t,
   z = bt,
   где а - диаметр спирали
       b - длина отрезка, на который переместится точка вдоль оси z при повороте на 1 радиан
       t - угол между положительным направлением оси x и радиусом (Функция)
        """

x1 = r1 * np.cos(t)
y1 = r1 * np.sin(t)
z1 = h * t

x2 = (r1 + r2 * np.sin(w * t)) * np.cos(t)
y2 = (r1 + r2 * np.sin(w * t)) * np.sin(t)
z2 = r2 * np.cos(w * t) + h * t


x3 = (r1 + r2 * np.sin(w * t) + r3 * np.cos(w2 * t)) * np.cos(t)
y3 = (r1 + r2 * np.sin(w * t) + r3 * np.sin(w2 * t)) * np.sin(t)
z3 = r2 * np.cos(w * t) + r3 * np.sin(w2 * t) + h * t

# Creating the plot
lines = []

line_marker = dict(color='#e62e00', width=32)
lines.append(go.Scatter3d(x=x1, y=y1, z=z1, mode='lines', line=line_marker))
line_marker = dict(color='#0066FF', width=20)
lines.append(go.Scatter3d(x=x2, y=y2, z=z2, mode='lines', line=line_marker))
line_marker = dict(color='#23660e', width=8)
lines.append(go.Scatter3d(x=x3, y=y3, z=z3, mode='lines', line=line_marker))

layout = go.Layout(
    title='Wireframe Plot',
    scene=dict(
        xaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        yaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        zaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        )
    ),
    showlegend=False,
)
fig = go.Figure(data=lines, layout=layout)
plot(fig, filename='wireframe_plot.html')
