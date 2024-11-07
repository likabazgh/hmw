import random

numbers = [random.randint(10, 1000000000) for _ in range(100)]

shortest = min(numbers, key=lambda x: len(str(x)))
longest = max(numbers, key=lambda x: len(str(x)))

sorted_asc = sorted(numbers, key=lambda x: len(str(x)))

sorted_desc = sorted(numbers, key=lambda x: len(str(x)), reverse=True)

print("Shortest: ", shortest)
print("Longest: ", longest)
print("Numbers sorted by length - ascending")
print(sorted_asc)
print("Numbers sorted by length - descending")
print(sorted_desc)