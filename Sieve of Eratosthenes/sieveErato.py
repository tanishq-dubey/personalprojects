import math


intInput = int(input("Enter prime search limit: "))
a = [True] * intInput

ieCounter = 0

for x in range(2, int(math.sqrt(intInput))):
    if a[x] is True:
        for j in range(x**2, intInput-1, x):
            ieCounter = ieCounter + 1
            a[j] = False

print("Primes found: ")
for q in range(0, len(a)-1):
    if a[q] is True:
        print(q)
