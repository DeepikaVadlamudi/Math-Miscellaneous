def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return ((b*a)/gcd(a,b))

print(lcm(3,5))
