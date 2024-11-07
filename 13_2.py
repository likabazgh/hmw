import random

list1 = [random.randint(1, 100) for _ in range(10)]
list2 = [random.randint(1, 100) for _ in range(10)]
list3 = [random.randint(1, 100) for _ in range(10)]

sums = [list1[i] + list2[i] + list3[i] for i in range(len(list1))]

print(list1)
print(list2)
print(list3)
print(sums)