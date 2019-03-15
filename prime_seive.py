def prime_seive(k):
    p=[1]*(k+1)
    p[0]=0
    p[1]=0
    for i in range(2,k+1):
        if p[i]==1:
            j=i+i
            while j<=k:
                p[j]=0
                j+=i
    return p
