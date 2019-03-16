def merge(A, B):
        l=[]
        i=0
        j=0
        while i<len(A) and j<len(B):
            if A[i]<B[j]:
                l.append(A[i])
                i+=1
            else:
                l.append(B[j])
                j+=1
        while i<len(A):
            l.append(A[i])
            i+=1
        while j<len(B):
            l.append(B[j])
            j+=1
        return l
