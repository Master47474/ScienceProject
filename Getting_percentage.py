#get how many people got 3/3,2/3,1/3,0/0 out of everyone
#the specify from each group
import matplotlib
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly
import plotly.graph_objs as go


one = 1
two = 2
three = 0

def get_averages(array,array2,array3,num1,num2,num3,outOf3,number):

    for scores in array:
        if scores == number:
            num3 = num3 + 1
    for scores in array2:
        if scores == number:
            num2 = num2+ 1
    for scores in array3:
        if scores == number:
            num1 = num1 + 1
    Plus = num3+num2+num1
    numAll = str(Plus)
    toFloat = float(Plus)
    numAverage = (toFloat / 11) * 100
    toStr = str(numAverage)
    print('the amount of ' + outOf3 + " = " + numAll)
    print("average number of " + outOf3 + " is " + toStr)
