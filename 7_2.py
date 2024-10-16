str_input = input("enter string: ")
lower_str = str_input.lower()

for i in range (0, len(str_input)):
    if str_input[i] != 'a' and str_input[i] != 'e' and str_input[i] != 'i' and str_input[i] != 'o' and str_input[i] != 'u':
        print(lower_str[i])
