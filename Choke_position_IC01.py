import datetime
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

inp = np.loadtxt('data/IC01_CHOKE_POSITION1.txt')
print(inp)

z = []
xchart = []
ychart = []

for i in range(288):
    ychart.append("Minute: " + str(i))
print(len(inp))

for i in range(int(len(inp)/288 + 1)):
    xchart.append("Day: " + str(i))
for i in range(len(xchart)):
    new_row = []
    for g in range(288):
        if not(i*288 + g+1 > len(inp)):
            new_row.append((np.log(inp[i*288 + g]) - np.log(72.75582982))/np.log(72.75582982))
        else:
            new_row.append("no data")
    z.append(list(new_row))

print(len(z[-1]))
print(len(z[0]))
print(len(z))
data = [
    go.Heatmap(
        z=z,
        y=xchart,
        x=ychart,
        colorscale='Greys',
    )
]

layout = go.Layout(
    title='Flow Control Valve(FCV) Pressure in %',
    xaxis = dict(ticks='', nticks=36),
    yaxis = dict(ticks='' )
)

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='choke_position-heatmap-IC01')
