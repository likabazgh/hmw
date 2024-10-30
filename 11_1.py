def convert_temperature(value, scale):
    if scale.upper() == 'C':
        return (value - 32) * 5 / 9
    elif scale.upper() == 'F':
        return value * 9 / 5 + 32


def main():
    input_1 = int(input("enter number: "))
    input_2 = int(input("enter number: "))
    input_3 = int(input("enter number: "))
    input_4 = int(input("enter number: "))


    print(f"100°F is {convert_temperature(input_1, 'C'):.2f}°C")
    print(f"0°C is {convert_temperature(input_2, 'F'):.2f}°F")
    print(f"32°F is {convert_temperature(input_3, 'C'):.2f}°C")
    print(f"100°C is {convert_temperature(input_4, 'F'):.2f}°F")


if __name__ == "__main__":
    main()