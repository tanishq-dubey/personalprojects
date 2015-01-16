digitStart = int(input("Enter a integer: "))

numberSteps = 0

while digitStart > 1:
    if digitStart % 2 == 0:
        digitStart = digitStart/2
        numberSteps = numberSteps + 1
    else:
        digitStart = (digitStart*3)+1
        numberSteps = numberSteps + 1

print("It took ", numberSteps, " steps to reach 1")
