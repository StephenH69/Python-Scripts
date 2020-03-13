# Write down a straightforward subtraction sum,
# A - B = C, where each of the numbers (A, B and C) 
# are made up of nine digits, 1 - 9 inclusive, with 
# each digit being used once only in each number.
import itertools
import math
import time

start_time = time.time()

originArray = [1,2,3,4,5,6,7,8,9]
numArray = []
numArrayR = []

# Create permutations
perms = list(itertools.permutations(originArray,9))

for nList in perms:
    str_nums = [str(x) for x in nList]
    num="".join(str_nums)
    numArray.append(int(num))

count = len(numArray)-1
while count>= 0:
    numArrayR.append(numArray[count])
    count -= 1

count = 0
maxCount = 20
for x in numArrayR:
    if x > (numArrayR[0]/2):
        for y in numArray:
            if y < x:
                result = x - y
                z = str(result)
                if ('1' in z) and ('2' in z) and ('3' in z) and ('4' in z) and ('5' in z) and ('6' in z) and ('7' in z) and ('8' in z) and ('9' in z):
                    txtP = "{} - {} = {}".format(str(x), str(y), str(result))
                    print(txtP)
                    count += 1
                if count == maxCount:
                    break
            if count == maxCount:
                break
        if count == maxCount:
            break
    if count == maxCount:
        break
            

print(count)
time_taken = time.time() - start_time
print("Time taken: ", str(time.time() - start_time))
