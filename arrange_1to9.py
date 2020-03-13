# Arrange these digits 1 2 3 4 5 6 7 8 9 to form:
# a three-digit multiple of three
# a three-digit multiple of four
# a three-digit multiple of five

import itertools
import time

start_time = time.time()

originArray = [1,2,3,4,5,6,7,8,9]
numArray, multiplesThree, multiplesFour, multiplesFive = [], [], [], []

perms = list(itertools.permutations(originArray,3))

for nList in perms:
    str_nums = [str(x) for x in nList]
    num="".join(str_nums)
    numArray.append(int(num))

for numb in numArray:
    if numb % 3 == 0: multiplesThree.append(numb)
    if numb % 4 == 0: multiplesFour.append(numb)
    if numb % 5 == 0: multiplesFive.append(numb)

uniqueThreesA = list(set(multiplesThree) - set(multiplesFour))
uniqueThrees = list(set(uniqueThreesA) - set(multiplesFive))

uniqueFoursA = list(set(multiplesFour) - set(multiplesThree))
uniqueFours = list(set(uniqueFoursA) - set(multiplesFive))

uniqueFivesA = list(set(multiplesFive) - set(multiplesThree))
uniqueFives = list(set(uniqueFivesA) - set(multiplesFour))

strThree, strFour, strFive = [], [], []
for unThree in uniqueThrees: strThree.append(str(unThree))
for unFour in uniqueFours: strFour.append(str(unFour))
for unFive in uniqueFives: strFive.append(str(unFive))

newList = list(itertools.product(strThree, strFour, strFive, repeat=1))

numArray2=[]
for newL in newList:
    newN = [str(x) for x in newL]
    numx="".join(newN)
    numArray2.append(numx)

print(len(numArray2))

count = 0
for z in numArray2:
    if ('1' in z) and ('2' in z) and ('3' in z) and ('4' in z) and ('5' in z) and ('6' in z) and ('7' in z) and ('8' in z) and ('9' in z):
        count += 1
        print(z[0:3:1] + ", " + z[3:6:1] + ", " + z[6::1])

print(count)
print("Time taken: ", time.time() - start_time)
