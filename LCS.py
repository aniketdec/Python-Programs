def rec(p,q,n,m):
        if n==0 or m==0:
                result=''
        elif p[n-1]==q[m-1]:
                result=p[n-1]+rec(p,q,n-1,m-1)
        else:
                t1=rec(p,q,n-1,m)
                t2=rec(p,q,n,m-1)
                if len(t1)>len(t2):
                        result=t1
                else:
                        result=t2
        return result
def lcs(p,q):
        ans=rec(p,q,len(p),len(q))
        ans=ans[::-1]
        return ans
