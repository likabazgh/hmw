input_num = int(input("write positive number: "))

for i in range(1, input_num + 1):
    if input_num % i == 0:
        print(i)