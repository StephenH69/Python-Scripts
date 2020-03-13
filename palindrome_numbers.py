number = int(input("Please enter any  whole number: "))

reverse = 0
temp = number

while temp > 0:
    Reminder = temp % 10
    reverse = (reverse * 10) + Reminder
    temp = temp // 10

print("The reverse of {} is {}.".format(number, reverse))

if number == reverse:
    print("%d is a Palindrome Number" % number)
else:
    print("%d is not a Palindrome Number" % number)
