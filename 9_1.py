def calculate(n):
    x = 0
    for i in range(n):
        term = (-1) ** i / (2 * i + 1)
        x += term
    x *= 4
    return x

for n in [10, 100, 10000, 100000]:
    approx = calculate(n)
    print(approx)
