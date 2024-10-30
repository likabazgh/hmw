def gcd_iterative(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd_iterative(a, b)

def main():
    a = int(input("Enter a 0 < a < 10000: "))
    b = int(input("Enter b 0 < b < 10000: "))
    if 0 < a < 10000 and 0 < b < 10000:
        lcm_value = lcm(a, b)

    print(f"LCM of {a} and {b} is {lcm_value}.")

if __name__ == "__main__":
    main()