##3 Do students from South Indian states really excel at Math and Science?
import pandas as pd
import numpy as nump
import matplotlib.pyplot as plt
df = pd.read_csv('nas-labels.csv')
stud = pd.read_csv('nas-pupil-marks.csv')
north = ['Jammu & Kashmir','Himachal Pradesh','Punjab','Chandigarh','Uttarakhand','Haryana','Delhi','Rajasthan','Uttar Pradesh']#NORTHEN STATES
south = ['Andaman & Nicobar', 'Andhra Pradesh', 'Karnataka', 'Kerala', 'Pondicherry', 'Tamil Nadu']#SOUTHERN STATES
d = {i[0]: i[1] for i in nump.array(df[['Level', 'Rename']])}#DICTIONARY OF CODES AND THEIR NAMES
data = nump.array(stud[['State', 'Maths %', 'Science %']])
south_sum = 0.0
north_sum = 0.0
str1 = []
str2 = []
s_codes = []
n_codes = []
for i in south:
    for key, val in d.iteritems():
        if(val == i):
            s_codes.append(key)
for i in north:
    for key, val in d.iteritems():
        if(val == i):
            n_codes.append(key)

#print s_codes
#print n_codes
sum1 = []
sum2 = []
for i in data:
    if(d[i[0]] in south and nump.isnan(i[1])== False and nump.isnan(i[2])== False):
        str1.append(d[i[0]])
        south_sum = south_sum+i[1]+i[2]
    elif(d[i[0]] in north and nump.isnan(i[1])== False and nump.isnan(i[2])== False):
        str2.append(d[i[0]])
        north_sum = north_sum+i[1]+i[2]
for i in s_codes:
    add=0
    for j in data:
        if(i==j[0] and nump.isnan(j[1]) == False):
            add = add+j[1]
    sum1.append(add)
for i in n_codes:
    add = 0
    for j in data:
        if(i==j[0] and nump.isnan(j[1]) == False):
            add = add+j[1]
    sum1.append(add)
final = []
for j in n_codes:
    s_codes.append(j)#append all the codes to s_codes for reprentation
x = [2, 4]
y = [south_sum, north_sum]
plt.title("Maths % for  South and North")
plt.bar(x, y, label='r')#BAR REPERSENTATION
plt.xlabel('States')
plt.ylabel('Maths %')
#plt.pie(sum1,labels=s_codes)#PIE REPRESENTATION OF MARKS RESPECTIVE STATES
#plt.legend()
plt.show()
