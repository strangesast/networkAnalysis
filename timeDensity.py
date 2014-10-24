import csv
import matplotlib.pyplot as plt
import time
import requests

postUrl = "http://api.macvendors.com/"

def process(string):
    return string[1:-2].split('","')

fname = 'captureDataRound2.csv'
with open(fname, 'r') as f:
    raw = f.readlines();
    header = process(raw[0])
    data = [process(x) for x in raw[1:]]

times = []
btimes = []
y = range(len(data));
y0 = []
y1 = []
#for i in [x for x in y if y.index(x)%100==0]:
#    row = data[i]
#    if row[3] == 'Broadcast':
#        btimes.append(float(row[1]))
#        y0.append(i)
#    else:
#        times.append(float(row[1]))
#        y1.append(i)

strengths = []
for row in data:
    try:
        x = float(row[-1][:-4])
        strengths.append(x)
    except:
        pass
    
uniqueLocs = set([x[3] for x in data])
u = []
for x in uniqueLocs:
    y =('').join([x[:2] for x in x.split(':')][-3:])
    if len(y) == 6:
        u.append(y)

destsHash = {}
for x in u:
    destsHash[x] = []

for row in data:
    dest = ('').join([x[:2] for x in row[3].split(':')][-3:])
    if len(dest) == 6:
        if dest in u:
            destsHash[dest].append(row)

for x in list(destsHash.items()):
    x = [float(x[-1][:-4]) for x in x[1]]
    print(len(x))

#plt.scatter(y0, btimes, 'ro', c='b', s=[float(20*n) for n in range(len(y0))])
#plt.plot(y1, times, 'o')
#plt.show()
