import matplotlib
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly
import plotly.graph_objs as go
import Making_Graphs


one = 1
two = 2
three = 3
zero = 0

def Count_average(array,name, num3, num2, num1,num,numOf):
    for scores in array:
        if scores == three:
            num3 = num3 + 3
        if scores == two:
            num2 = num2 + 2
        if scores == one:
            num1 = num1 + 1
        if scores == zero:
            num = num + 0
    Plus = num3 + num2 + num1 + num
    numAll = str(Plus)
    toFloat = float(Plus)
    numAverage = (toFloat / numOf)
    toStr = str(numAverage)
    Making_Graphs.MakeGraphAverage(name,numAverage)