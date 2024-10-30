def gcd_iterative(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

def main():
    a = int(input("enter number: "))
    b = int(input("enter number: "))

    if 0 < a < 10000 and 0 < b < 10000:
        gcd_iter = gcd_iterative(a, b)
        gcd_recur = gcd_recursive(a, b)

        print(f"gcd of {a} and {b} iterative is {gcd_iter}.")
        print(f"gcd of {a} and {b} recursive is {gcd_recur}.")
    else:
        print("must be between 1 and 9999.")

if __name__ == "__main__":
    main()