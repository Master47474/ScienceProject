import matplotlib
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly
from plotly.graph_objs import Scatter, Layout
#"layout": Layout(title="hello world")


def MakeGraph(name,num3,num2,num1,num):
    data = [plotly.graph_objs.Bar(
        x=['0/3','1/3','2/3','3/3'],
        y= [num,num1,num2,num3]
    )]
    layout = plotly.graph_objs.Layout(title=name)
    fig = plotly.graph_objs.Figure(data=data,layout=layout)
    plotly.offline.plot(fig, filename= 'graph-make')

def MakeGraphAverage(name,AverageNum):
    dataA = [plotly.graph_objs.Scatter(
        x=[name],
        y=[AverageNum]
    )]
    layout = plotly.graph_objs.Layout(title= name + "Avergage Score")
    fig = plotly.graph_objs.Figure(data=dataA,layout=layout)
    plotly.offline.plot(fig,filename = "graph-Average")