import random

def generate_choice():
    return random.choice(['r', 's', 'p'])

def main():
    user_choice = input("enter your choice").lower()
    rand_choice = generate_choice()

    if(user_choice == rand_choice):
        print("draw")
    if(user_choice == 'r' and rand_choice == 's') or \
      (user_choice == 's' and rand_choice == 'p') or \
      (user_choice == 'p' and rand_choice == 'r'):
        print("user wins")
    else:
        print("computer wins")

if __name__ == "__main__":
    main()

