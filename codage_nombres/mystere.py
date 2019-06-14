from decimal import *
import numpy as np

def mystere():
    a=1.0
    i=0
    while(((a+1.0) - a) == 1.0):
        a *= 2.0
        i+=1
    b = 1.0
    while (((a + b) - a) != b):
        b += 1

    return i,b

def mystere_autres_float(one, two):
    i = 0
    a = one
    b= one
    while (((a + one) - a) == one):
        a *= two
        i += 1

    while (((a + b) - a) != b):
        b += one

    return i, b

print(f'{mystere()}')

print(f'{mystere_autres_float(np.float16(1.0),np.float16(2.0))}')
print(f'{mystere_autres_float(np.float32(1.0),np.float32(2.0))}')
print(f'{mystere_autres_float(np.float64(1.0),np.float64(2.0))}')
print(f'{mystere_autres_float(Decimal(1.0),Decimal(10.0))}')