import datetime
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

inp = np.loadtxt('data/ESP02_MOTOR_TEMP.txt')
print(inp)

z = []
ztxt = []
xchart = []
ychart = []

for i in range(288):
    ychart.append("Minute: " + str(i*5))
print(len(inp))

for i in range(int(len(inp)/288 + 1)):
    xchart.append("Day: " + str(i))
for i in range(len(xchart)):
    new_row = []
    txt_row = []
    for g in range(288):
        if not(i*288 + g+1 > len(inp)):
            new_row.append((np.log(inp[i*288 + g]) - np.log(372))/np.log(372))
            txt_row.append(str(inp[i*288 + g]) + "K")
        else:
            new_row.append("no data")
            txt_row.append("no data")
    z.append(list(new_row))
    ztxt.append(list(txt_row))

print(len(z[-1]))
print(len(z[0]))
print(len(z))
data = [
    go.Heatmap(
        z=z,
        text=ztxt,
        y=xchart,
        x=ychart,
        colorscale='Greys',
    )
]

layout = go.Layout(
    title='Motor Temperature in Kelvin ESP02',
    xaxis = dict(ticks='', nticks=36),
    yaxis = dict(ticks='' )
)

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='temp-heatmap-motor-ESP02')
