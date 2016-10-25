import Getting_Scores
import Gathering_deatails
import Getting_percentage
import GetAverage
import matplotlib
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly
import plotly.graph_objs as go

file = open("Readme.txt", 'r')
data = file.read()
rows = data.split('\n')
data_split = rows[1:len(rows)]

stats = []

Ad3 = 0
Ad2 = 0
Ad1 = 0
Ad0 = 0

Md3 = 0
Md2 = 0
Md1 = 0
Md0 = 0

Gd3 = 0
Gd2 = 0
Gd1 = 0
Gd0 = 0


#get score
def get_score(array):
    for Score in array:
        if Score == "3/3":
            Getting_Scores.Ascore3 =+ 3
            array.append(Getting_Scores.Ascore3)
        if Score == "2/3":
            Getting_Scores.Ascore2 =+ 2
            array.append(Getting_Scores.Ascore2)
        if Score == "1/3":
            Getting_Scores.Ascore1 =+ 1
            array.append(Getting_Scores.Ascore1)
        if Score == "0/3":
            Getting_Scores.Ascore0 =+ 0
            array.append(Getting_Scores.Ascore0)
for row in data_split:
    row_data = row.split(',')
    stats.append(row_data)



#main loop for sorting out data
def get_Stats():
    for stat in stats:
        if 'advanced' == stat[2]:
            Getting_Scores.Advanced10.append(stat[2])
            Getting_Scores.Advanced_firstQ(stat[3])
            Getting_Scores.Advanced_secondQ(stat[4])
            Getting_Scores.Advanced_thirdQ(stat[5])
            Getting_Scores.Advanced10.append(stat[6])
            get_score(Getting_Scores.Advanced10)
        if 'methods' == stat[2]:
            Getting_Scores.Methods10.append(stat[2])
            Getting_Scores.Method_firstQ(stat[3])
            Getting_Scores.Method_secondQ(stat[4])
            Getting_Scores.Method_thirdQ(stat[5])
            Getting_Scores.Methods10.append(stat[6])
            get_score(Getting_Scores.Methods10)
        if 'general' == stat[2]:
            Getting_Scores.General10.append(stat[2])
            Getting_Scores.General_firstQ(stat[3])
            Getting_Scores.General_secondQ(stat[4])
            Getting_Scores.General_thirdQ(stat[5])
            Getting_Scores.General10.append(stat[6])
            get_score(Getting_Scores.General10)
        print(Getting_Scores.Advanced10)
        Gathering_deatails.Count_score(Getting_Scores.Advanced10[len(Getting_Scores.Advanced10) - 9:len(Getting_Scores.Advanced10)], "Advanced",Ad0, Ad1, Ad2, Ad3)
        print(Getting_Scores.Methods10)
        Gathering_deatails.Count_score(Getting_Scores.Methods10[len(Getting_Scores.Methods10) - 9:len(Getting_Scores.Methods10)], "Methods", Md0, Md1, Md2, Md3)
        print(Getting_Scores.General10)
        Gathering_deatails.Count_score(Getting_Scores.General10[len(Getting_Scores.General10) - 6:len(Getting_Scores.General10)], "General", Gd0, Gd1, Gd2, Gd3)
        Getting_percentage.get_averages(Getting_Scores.Advanced10[len(Getting_Scores.Advanced10) - 9:len(Getting_Scores.Advanced10)],Getting_Scores.Methods10[len(Getting_Scores.Methods10) - 9:len(Getting_Scores.Methods10)],Getting_Scores.General10[len(Getting_Scores.General10) - 6:len(Getting_Scores.General10)],Ad3,Md3,Gd3,"3/3",3)
        Getting_percentage.get_averages(Getting_Scores.Advanced10[len(Getting_Scores.Advanced10) - 9:len(Getting_Scores.Advanced10)], Getting_Scores.Methods10[len(Getting_Scores.Methods10) - 9:len(Getting_Scores.Methods10)], Getting_Scores.General10[len(Getting_Scores.General10) - 6:len(Getting_Scores.General10)],Ad2, Md2, Gd2, "2/3",2)
        Getting_percentage.get_averages(Getting_Scores.Advanced10[len(Getting_Scores.Advanced10) - 9:len(Getting_Scores.Advanced10)], Getting_Scores.Methods10[len(Getting_Scores.Methods10) - 9:len(Getting_Scores.Methods10)], Getting_Scores.General10[len(Getting_Scores.General10) - 6:len(Getting_Scores.General10)],Ad1, Md1, Gd1, "1/3",1)
        Getting_percentage.get_averages(Getting_Scores.Advanced10[len(Getting_Scores.Advanced10) - 9:len(Getting_Scores.Advanced10)], Getting_Scores.Methods10[len(Getting_Scores.Methods10) - 9:len(Getting_Scores.Methods10)], Getting_Scores.General10[len(Getting_Scores.General10) - 6:len(Getting_Scores.General10)],Ad1, Md1, Gd1, "0/3",0)
        #gettting average for each one
        GetAverage.Count_average(Getting_Scores.Advanced10[len(Getting_Scores.Advanced10) - 9:len(Getting_Scores.Advanced10)],"advanced",Ad3,Ad2,Ad1,Ad0,4)
        GetAverage.Count_average(Getting_Scores.Methods10[len(Getting_Scores.Methods10) - 9:len(Getting_Scores.Methods10)],"Methods",Md3,Md2,Md1,Md0,4)
        GetAverage.Count_average(Getting_Scores.General10[len(Getting_Scores.General10) - 6:len(Getting_Scores.General10)], "General", Gd3,Gd2, Gd1, Gd0,3)



get_Stats()
