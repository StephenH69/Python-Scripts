 # Python Program to print Prime Numbers from 1 to n
import time

minimum = int(input("Please Enter the Minimum Value:"))
maximum = int(input("Please Enter the Maximum Value:"))

Number = minimum

sum = 0

start = time.time()

while(Number <= maximum):
    count = 0
    i = 2
    
    while(i <= Number//2):
        if(Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')
        sum += Number
    Number = Number  + 1


elapsed = (time.time() - start)


print("\n\n" + str(sum) + "\n")
print ("Finished in %s seconds" % (elapsed))