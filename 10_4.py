def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

int_1 = int(input("enter number: "))
int_2 = int(input("enter number: "))
int_3 = int(input("enter number: "))

print(is_prime(int_1))
print(is_prime(int_2))
print(is_prime(int_3))