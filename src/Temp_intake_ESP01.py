import datetime
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

inp = np.loadtxt('data/intake_temp.txt')
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
            new_row.append((np.log(inp[i*288 + g]) - np.log(390.8))/np.log(390.8))
            txt_row.append(str(inp[i*288 + g])+"K")
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
        text = ztxt,
        y=xchart,
        x=ychart,
        colorscale=
        [[0.0, 'rgb(49,54,149)'],
        [0.1111111111111111, 'rgb(69,117,180)'],
        [0.1515151515151515, 'rgb(116,173,209)'],
        [0.2222222222222222, 'rgb(171,217,233)'],
        [0.2626262626262626, 'rgb(224,243,248)'],
        [0.3333333333333333, 'rgb(254,224,144)'],
        [0.3939393939393939, 'rgb(253,174,97)'],
        [0.5959595959595959, 'rgb(244,109,67)'],
        [0.8888888888888888, 'rgb(215,48,39)'],
        [1.0, 'rgb(165,0,38)']]
    )
]


layout = go.Layout(
    title='Temperature Intake in kelvin ESP01',
    xaxis = dict(ticks='', nticks=36),
    yaxis = dict(ticks='' )
)

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='temp-heatmap-intake-ESP01')
