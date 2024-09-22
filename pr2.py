import random

input_num = int(input("write integer number less than 30: "))

n = 0

for i in range(input_num):
    num = random.randint(0, 1000)
    if(num > n):
        n = num
    
print(n)