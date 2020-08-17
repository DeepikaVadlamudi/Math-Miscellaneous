def Euclidean(a,b):
    if b==0:
        return a
    return Euclidean(b,a%b)

print(Euclidean(18,324))
