n = int(input("Enter number less than 20: "))

a = 0
b = 1
count = 0

while count <= n:
    print(a, end=' ')
    temp = a
    a = b
    b = temp + b 
    count += 1