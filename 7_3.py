str_input = input("enter string: ")
length = len(str_input)

middle = str_input[(length - 1) // 2 : (length + 2) // 2]
    
first = str_input[0]
last = str_input[-1]

i = 0

while i < 5:
    print(first, last, middle)
    i += 1
