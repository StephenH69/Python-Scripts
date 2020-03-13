# Will calculate the nth term formula in a linear sequence, with the formula:
# nth term = dn + (a - d)

# Will check the nth term in a non-linear equation using the formula:
# nth term = (c/2)n2 + dn - (c3/2)n + a + c - d




# Check if linear or non linear
def checkIfLinear (the_sequence):
    isLinear = True
    j, diff, new_diff= 0, 0, 0
    while j < (len(the_sequence) - 1):
        new_diff = abs(the_sequence[j]-the_sequence[j+1])
        if j == 0:
            diff = new_diff
        elif diff != new_diff:
            isLinear = False
        j += 1
    return isLinear, diff

# Create the linear equation
def linear_calc(the_sequence, diff):
    print("Sequence is linear.")
    second_number =  the_sequence[0] - diff
    if second_number != 0:
        if second_number > 0 :
            the_formula = "nth term = " + str(diff) + "n + " + str(second_number)
        else:
            the_formula = "nth term = " + str(diff) + "n " + str(second_number)
    else:
        the_formula = "nth term = " + str(diff) + "n"
    return the_formula

# Create the non-linear equation
def non_linear_calc(the_sequence, diff):
    k, l = 0, 0
    second_sequence, third_sequence = [], []
    print("Sequence is non-linear.")
    while k < len(the_sequence) - 1:    
        diff = second_sequence.append(the_sequence[k+1] - the_sequence[k])
        k += 1

    while l < len(second_sequence) - 1:
        diff = third_sequence.append(second_sequence[l+1] - second_sequence[l])
        l += 1

    if (third_sequence[0] % 2) == 0:
        first_no = int(third_sequence[0]/2)
    else:
        first_no = third_sequence[0]/2
    if ((third_sequence[0]*3) % 2) == 0:
        second_no = int(second_sequence[0]) - int(((third_sequence[0]*3)/2))
    else:
        second_no = second_sequence[0] - ((third_sequence[0]*3)/2)
    third_no = the_sequence[0] + third_sequence[0] - second_sequence[0]

    if third_no != 0 and second_no != 0:
        if third_no > 0:
            the_formula = "nth term = " + str(first_no) + "n2 + " + str(second_no) + "n + " + str(third_no)
        else:
            the_formula = "nth term = " + str(first_no) + "n2 + " + str(second_no) + "n " + str(third_no)
    elif  third_no == 0 and second_no == 0:
        the_formula = "nth term = " + str(first_no) + "n2"
    elif third_no == 0 and second_no != 0:
        the_formula = "nth term = " + str(first_no) + "n2 + " + str(second_no) + "n"
    elif third_no != 0 and second_no == 0:
        the_formula = "nth term = " + str(first_no) + "n2 + " + str(third_no)
    return the_formula


the_sequence = []

n = int(input("Enter number of elements in the sequence, followed by the elements: "))

for i in range(0, n): 
    ele = int(input()) 
    the_sequence.append(ele) 

print(the_sequence)

# Check if linear or non linear
is_linear, diff = checkIfLinear(the_sequence)

if is_linear == True:
    print(linear_calc(the_sequence, diff))
else:
    print(non_linear_calc(the_sequence, diff))


# Non linear sequences:
# 6, 17, 34, 57, 86     3n2 + 2n + 1
# 4, 13, 26, 43, 64     2n2 + 3n - 1

# Linear sequence
# 4, 15, 26, 37, 48     11n - 7