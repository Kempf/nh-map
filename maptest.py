import csv
import matplotlib.pyplot as plt
import numpy as np

fon_min = [[0 for i in range(102)] for j in range(205)]
fon_max = [[0 for i in range(102)] for j in range(205)]

with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        x = int(float(row["X"])*10)
        
        y = int(float(row["Y"])*10)
#        print(x,y,row["min"],row["max"])
        fon_min[y][x]=int(row["min"])
        fon_max[y][x]=int(row["max"])
#print(fon_max)

im = plt.imread("map.png")
plt.style.use('_mpl-gallery-nogrid')
fig, ax = plt.subplots()
ax.imshow(im, extent=[0,102,205,0])
plot = ax.imshow(fon_max, alpha=0.5, cmap="magma_r")
fig.colorbar(plot,label="mSv/hr")
plt.show()