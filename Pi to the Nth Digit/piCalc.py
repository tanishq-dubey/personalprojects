import math
from math import factorial
from decimal import *


digitAccuracy = int(input("Enter the digit of Pi to calculate to: "))
digitCounter = int(input("Enter desired accuracy of calulation: "))

getcontext().prec = int(digitAccuracy)

pi = Decimal(0)
k = 0
while k < digitCounter:
    pi += (Decimal(-1) ** k) * (Decimal(factorial(6 * k)) / ((factorial(k) ** 3) * (factorial(3 * k))) * (13591409 + 545140134 * k) / (640320 ** (3 * k)))
    k = k + 1
pi = pi * Decimal(10005).sqrt()/4270934400
pi = pi**(-1)

accuracy = 100*((Decimal(math.pi)-pi)/pi)

print("Pi is about: ", pi)
print("Error is about: ", accuracy, "%")
