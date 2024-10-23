import random
import math

def calculate(n):
    counter = 0
    for _ in range(n):
        a = random.uniform(0, 1)
        b = random.uniform(0, 1)

        if math.sqrt(a ** 2 + b ** 2) <= 1:
            counter += 1

    calculate = 4 * counter / n
    return calculate

n = int(input("Enter number: "))
approx = calculate(n)
print(approx)
