import math

def isPrime(n):
    if(n<=1):
        return False
    if(n==2):
        return True
    if(n%2==0):
        return False
    m=math.isqrt(n)
    for i in range(3,m):
        if(n%i==0):
            return False

    return True

n=21
g=isPrime(n)
print(g)
