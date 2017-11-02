##2 How do boys and girls perform across states?
import pandas as pd
import numpy as nump
import matplotlib.pyplot as plt
df = pd.read_csv("nas-labels.csv")#read labels
pupil = pd.read_csv("nas-pupil-marks.csv")#read marks
boy = 1
girl = 2
#print df[['Level', 'Rename']]
d = {i[0]: i[1] for i in nump.array(df[['Level', 'Rename']])}
#print d
arr = nump.array(df[['Column', 'Level', 'Rename']])
#print arr
state = {i[1]: i[2] for i in arr if(i[0] == 'State')}
#print state
perf = nump.array(pupil[['State', 'Gender', 'Maths %', 'Reading %', 'Science %', 'Social %']])
#print perf
marks = {}
boys = []
girls = []
for i in state:
    add1 = 0.0
    add2 = 0.0
    for j in perf:
        if j[0] == i:
            if(j[1]==boy):
                if nump.isnan(j[2]) == False : add1 = add1 + j[2]#check if the value is a number
                if nump.isnan(j[3]) == False : add1 = add1 + j[3]
                if nump.isnan(j[4]) == False : add1 = add1 + j[4]
                if nump.isnan(j[5]) == False : add1 = add1 + j[5]

            elif (j[1] == girl):
                if nump.isnan(j[2]) == False : add2 = add2 + j[2]
                if nump.isnan(j[3]) == False : add2 = add2 + j[3]
                if nump.isnan(j[4]) == False : add2 = add2 + j[4]
                if nump.isnan(j[5]) == False : add2 = add2 + j[5]

    boys.append(add1)
    girls.append(add2)
#print boys
x1 = [2*n for n in range(33)]
y1 = boys
x2 = [2*n+1 for n in range(33)]
y2 = girls
plt.plot(x1, y1, label='Boys', color='r')#plot a line of boys across states
plt.plot(x2, y2, label='Girls', color='c')#plot a line of girls across states
plt.legend()
plt.show()