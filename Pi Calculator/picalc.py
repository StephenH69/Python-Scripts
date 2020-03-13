from math import factorial
from decimal import Decimal, getcontext
import time

def classic(n):
    getcontext().prec = n
    t= Decimal(0)
    pi = Decimal(0)
    deno= Decimal(0)
    k = 0
    for k in range(n):
        t = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
        deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
        pi += Decimal(t)/Decimal(deno)                                   
    pi = pi * Decimal(12)/Decimal(640320**Decimal(1.5))
    pi = 1/pi
    return pi


def leibniz(iteration,dec):
    # 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + 4/13 - 4/15 + 4/17 - 4/19....
    getcontext().prec = dec
    piresult = Decimal(4)
    i = 1
    while i < (iteration + 1):
        if i % 2 == 0:
            piresult += Decimal(4/((i*2)+1))
        else:
            piresult -= Decimal(4/((i*2)+1))
        i += 1
    return piresult

def nilakantha(iteration,dec):
    # 3 + 4/(2x3x4) - 4/(4x5x6) + 4/(6x7x8) - 4/(8x9x10) + 4/(10x11x12)....
    getcontext().prec = dec
    piresult = Decimal(3)
    i = 1
    while i < (iteration + 1):
        if i % 2 == 0:
            piresult -= Decimal(4/((i*2) * ((i*2) + 1) * ((i*2) + 2)))
        else:
            piresult += Decimal(4/((i*2) * ((i*2) + 1) * ((i*2) + 2)))
        i += 1
    return piresult