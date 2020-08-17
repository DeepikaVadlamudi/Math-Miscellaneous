def SoE(n):
    prime_num_list=[True for i in range(n+1)]
    p=2
    while(p*p<=n):
        if(prime_num_list[p]):
            for i in range(p*p,n+1,p):
                prime_num_list[i]=False
        p+=1
    for i in range(n+1):
        if(prime_num_list[i]):
            print(i)

n=100
SoE(n)
