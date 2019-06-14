import math

def u(n):
    if n == 0:
        return 1
    return u(n - 1) + (-1)**n * 10 ** n / math.factorial(n)

def v(n):
    if n==0:
        return 1
    return v(n-1)+10**n/math.factorial(n)

def serie_u(n):
    sum=0.0
    term=1.0
    for k in range(1,n+1):
        sum+=term
        term*=-10/k
        k+=1
    return sum

print(f'e(-10) = {u(100)}')
print(f'e(-10) = {serie_u(100)}')
print(f'e(-10) = {1/v(100)}')