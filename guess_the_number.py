import random

max_num = int(input("Welcome to guess the number.\nPlease enter the maximum number I can think of:"))
secret_number = random.randint(1, max_num)
guess_count = 0
error_count = 0
correct_guess = 0

print("I've thought of a number between 1 and {}".format(max_num))

# print(secret_number)


def guess_calc(s, g):
    if g == s:
        return "Correct"
    elif g < s:
        return "Low"
    else:
        return "High"


while error_count < 5 and correct_guess == 0:
    guess = input("Please enter your guess:")

    try:
        your_guess = int(guess)
    except ValueError:
        your_guess = 0

    if 0 < your_guess < max_num:
        guess_count += 1
        error_count = 0
        guess_status = guess_calc(secret_number, your_guess)
        if guess_status == "Correct":
            print("Well done you guessed the correct number.\nThis was guess number {}".format(guess_count))
            correct_guess = 1
        elif guess_status == "Low":
            print("Your guess is too low, try again.")
        else:
            print("Your guess is too high, try again.")

    else:
        if error_count < 4:
            guess_count += 1
            print("You don't quite get this do you?.\nGo on try again.\n")
            print("Your number must be between 1 and {} inclusive.\n".format(max_num))
        else:
            print("You are obviously too stupid to play such a simple game - goodbye")
        error_count += 1
