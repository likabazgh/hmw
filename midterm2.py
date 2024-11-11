


input_num = int(input("write number 10 <= n <= 5432: "))
if input_num < 10 or input_num > 5432:
    print("wrong input number")

count = 0
curr_num = 13

while curr_num <= input_num:
    print(curr_num)
    count += 1
    curr_num += 13

print(f"number of this nums: {count }")






