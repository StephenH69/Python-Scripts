import picalc
from math import factorial
from decimal import Decimal, getcontext
import time

def main():

    errorCount = 0
    numberOfDigitsString = "Please enter the number of decimal places to calculate Pi to: "
    numberOfIterationsString = "Please enter the number of iterations for the calculation of Pi: "
    goAgainString = "Do you want to run the program again? [Y/N]: "

    while errorCount < 5:
        try:
            theSelection = int(input("Please select the style of calculation:\n1 - Classic\n2 - Gregory Leibniz\n3 - Nilakantha\nYour selection: "))
        except ValueError:
            theSelection = 9

        if theSelection == 1:
            numberofdigits = int(input(numberOfDigitsString))

            start_time = time.time()
            print(picalc.classic(numberofdigits))
            print("Time taken: ", time.time() - start_time)

            goAgain = input(goAgainString)
            if goAgain.upper() != 'Y':
                break
            errorCount = 0

        elif theSelection == 2:
            numberofdigits = int(input(numberOfDigitsString))
            iterations = int(input(numberOfIterationsString))

            start_time = time.time()
            print(picalc.leibniz(iterations,numberofdigits))
            print("Time taken: ", time.time() - start_time)

            goAgain = input(goAgainString)
            if goAgain.upper() != 'Y':
                break
            errorCount = 0

        elif theSelection == 3:
            numberofdigits = int(input(numberOfDigitsString))
            iterations = int(input(numberOfIterationsString))

            start_time = time.time()
            print(picalc.nilakantha(iterations,numberofdigits))
            print("Time taken: ", time.time() - start_time)

            goAgain = input(goAgainString)
            if goAgain.upper() != 'Y':
                break
            errorCount = 0


        else:
            if errorCount < 4:
                print("You don't quite get this do you?.\nGo on try again.\n")
            else:
                print("You are obviously too stupid for such basic instructions - goodbye")
            errorCount += 1


if __name__ == '__main__':
    main()