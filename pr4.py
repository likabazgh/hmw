input_num = int(input("write number: "))
first = 0
second = 1

if input_num == 0:
    print(first)
elif input_num == 1:
    print(second)

for i in range(2, input_num + 1):
    next = first + second
    first = second
    second = next
    
print(next)