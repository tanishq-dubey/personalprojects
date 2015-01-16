import math
import os


clear = lambda: os.system('cls')
x = 0
y = 0
whileCounter = 0
xCoord = []
yCoord = []
minDistance = 9999999999999999
minIndexOne = 99999999999999
minIndexOne = 99999999999999


while x < 1000:
    x = float(input("Enter the x coordinate: "))
    y = float(input("Enter the y coordinate: "))
    xCoord.append(x)
    yCoord.append(y)

for j in range(0, len(xCoord)-1):
    for i in range(j+1, len(xCoord)-1):
        minTempDistance = math.sqrt(((xCoord[i]-xCoord[j])**2)+((yCoord[i]-yCoord[j])**2))
        if minTempDistance < minDistance:
            minDistance = minTempDistance
            minIndexOne = j
            minIndexTwo = i
            pass
    pass

print("The minimum distance is between the points (", xCoord[minIndexOne], ",", yCoord[minIndexOne], ") and (", xCoord[minIndexTwo], ",", yCoord[minIndexTwo], ") with the value of ", minDistance)
