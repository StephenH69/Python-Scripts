import random

dict_options = {1: "Rock", 2: "Paper", 3: "Scissors"}
winner = "Me"
me_i = 0
you_i = 0
error_count = 0


def did_you_win(m, y):
    if (m == 1) and (y == 2):
        return "You"
    elif (m == 1) and (y == 3):
        return "Me"
    elif (m == 2) and (y == 3):
        return "You"
    elif (m == 2) and (y == 1):
        return "Me"
    elif (m == 3) and (y == 1):
        return "You"
    elif (m == 3) and (y == 2):
        return "Me"
    else:
        return "Draw"


while error_count < 5:
    print("Choose your weapon:\n1 - Rock\n2 - Paper\n3 - Scissors")
    my_selection = random.randint(1, 3)
    selection = input("Please select 1, 2 or 3: ")

    try:
        your_selection = int(selection)
    except ValueError:
        your_selection = 4

    if (your_selection == 1) or (your_selection == 2) or (your_selection == 3):
        error_count = 0
        print("\nI chose {} - {}".format(my_selection, dict_options[my_selection]))
        print("You chose {} - {}\n".format(your_selection, dict_options[your_selection]))
        winner = did_you_win(my_selection, your_selection)
        if winner == "Me":
            me_i += 1
            print("I won!\n\nI've won {}\nYou've won {}\n".format(me_i, you_i))
        elif winner == "You":
            you_i += 1
            print("You won!\n\nI've won {}\nYou've won {}\n".format(me_i, you_i))
        else:
            print("It's a draw!\n\nI've won {}\nYou've won {}\n".format(me_i, you_i))
    else:
        if error_count < 4:
            print("You don't quite get this do you?.\nGo on try again.\n")
        else:
            print("You are obviously too stupid to play such a simple game - goodbye")
        error_count += 1
