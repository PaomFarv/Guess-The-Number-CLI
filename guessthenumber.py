import random
try:
    guessing_range = int(input("Insert the Range: "))
except ValueError:
    print("It must be a number greater than 0.")
    quit()

random_number = random.randint(0,guessing_range)
print("Computer has chosen a number.")
while True:
    try:
        user_guess = int(input("Make a Guess: "))
    except ValueError:
        print("Input must be a number.")
        exit()

    if user_guess == random_number:
        print("Damn!You're Correct.")
        break

    elif user_guess > random_number:
        print("You are above the number.")

    elif user_guess < random_number:
        print("You are below the number.")

print("Run this script again to play again.")