import matplotlib
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly
import plotly.graph_objs as go


Advanced10 = []
Methods10 = []
General10 = []

correct_answer1 = "correct1"
correct_answer2 = "correct2"
correct_answer3 = "correct3"
countera = 1
counterm = 1
counterg = 1

Ascore3 = 0
Ascore2 = 0
Ascore1 = 0
Ascore0 = 0

Mscore3 = 0
Mscore2 = 0
Mscore1 = 0
Mscore0 = 0

Gscore3 = 0
Gscore2 = 0
Gscore1 = 0
Gscore0 = 0
def Advanced_firstQ(FirstQ):
    if FirstQ == "correct":
        Advanced10.append(correct_answer1)
    else:
        Advanced10.append("incorrect1")
def Advanced_secondQ(second):
    if second == "correct":
        Advanced10.append(correct_answer2)
    else:
        Advanced10.append("incorrect2")
def Advanced_thirdQ(third):
    if third == "correct":
        Advanced10.append(correct_answer3)
    else:
        Advanced10.append("incorrect3")

def Method_firstQ(FirstQ):
    if FirstQ == "correct":
        Methods10.append(correct_answer1)
    else:
        Methods10.append("incorrect1")
def Method_secondQ(second):
    if second == "correct":
        Methods10.append(correct_answer2)
    else:
        Methods10.append("incorrect2")
def Method_thirdQ(third):
    if third == "correct":
        Methods10.append(correct_answer3)
    else:
        Methods10.append("incorrect3")

def General_firstQ(FirstQ):
    if FirstQ == "correct":
        General10.append(correct_answer1)
    else:
        General10.append("incorrect1")
def General_secondQ(second):
    if second == "correct":
        General10.append(correct_answer2)
    else:
        General10.append("incorrect2")
def General_thirdQ(third):
    if third == "correct":
        General10.append(correct_answer3)
    else:
        General10.append("incorrect3")