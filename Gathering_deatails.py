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

def Count_score(array,name, num, num1, num2,num3):
    for scores in array:
        if scores == three:
            num3 = num3 + 1
        if scores == two:
            num2 = num2 + 1
        if scores == one:
            num1 = num1 + 1
        if scores == zero:
            num = num + 1
    num3 = str(num3)
    print(name + ' 3/3 =' + num3)
    num2 = str(num2)
    print(name + ' 2/3 =' + num2)
    num1 = str(num1)
    print(name + ' 1/3 =' + num1)
    num = str(num)
    print(name + ' 0/3 =' + num)
    Making_Graphs.MakeGraph(name,num3,num2,num1,num)



