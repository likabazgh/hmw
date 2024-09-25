num = int(input("write number less than 50: "))

for n in range(1, num + 1):
        divisors = []
        for i in range(1, n + 1):
            if n % i == 0:
                divisors.append(i)

print(divisors[:3])