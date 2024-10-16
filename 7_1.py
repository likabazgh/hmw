str_input = input("enter string: ")

for i in range (0, len(str_input), 2):
    if str_input[i] != 'e':
        print(str_input[i])