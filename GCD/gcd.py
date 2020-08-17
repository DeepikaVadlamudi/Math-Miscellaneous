import math

def GCD(a,b):
    i=min(a,b)
    while(i>=1):
        if(a%i==0 and b%i==0):
            return i
        i-=1

print(GCD(12,18))
