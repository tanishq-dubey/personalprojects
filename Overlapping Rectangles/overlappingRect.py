#test input is 1,1,3,3.-2,-2,2,2
#These squares ARE overlapping, so the program should return true

inputString = "1,1,3,3,-2,-2,4,4"

inputPoints = inputString.split(",")

#print(inputPoints)

inputPoints = list(map(int, inputPoints))

#print(inputPoints)

isIntersecting = False

rectOneTop = inputPoints[0:2]  # Should hold 1,1
rectOneBot = inputPoints[2:4]  # Should hold 3,3

rectTwoTop = inputPoints[4:6]  # Should hold 3,3
rectTwoBot = inputPoints[6:9]  # Should hold 3,3

#print(rectOneTop)
#print(rectOneBot)
#print(rectTwoTop)
#print(rectTwoBot)

rectOneTopTwo = inputPoints[0:3:2]
rectOneBotTwo = inputPoints[2::-2]

rectTwoTopTwo = inputPoints[4:7:2]
rectTwoBotTwo = inputPoints[7:4:-2]

#print("==========")

#print(rectOneTopTwo)
#print(rectOneBotTwo)
#print(rectTwoTopTwo)
#print(rectTwoBotTwo)

#print("===========")

for x in range(0, 1):
    if rectOneTop[0] in range(*sorted((rectTwoBot[0], rectTwoTop[0]))):
        if rectOneTop[1] in range(*sorted((rectTwoBot[1], rectTwoTop[1]))):
            isIntersecting = True
    if rectOneBot[0] in range(*sorted((rectTwoBot[0], rectTwoTop[0]))):
        if rectOneBot[1] in range(*sorted((rectTwoBot[1], rectTwoTop[1]))):
            isIntersecting = True

print(isIntersecting)
