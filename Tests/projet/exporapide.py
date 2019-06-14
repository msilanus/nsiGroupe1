import math

def expo_rapide(x, n):
    if (x == 0):
        return 0
    if(n==0):
        return 1
    if(n==1):
        return(x)
    if((n%2)==0):
            return (expo_rapide(x ** 2, n / 2))

    return (x * expo_rapide(x ** 2, (n - 1) / 2))

def main():
    print(expo_rapide(2, 12))

if __name__ == "__main__":
    main()