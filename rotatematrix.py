def rotate(matrix):
        n=len(matrix[0])-1
        o=n
        for  x in range(len(matrix[0])/2):
            a,b=x,x
            c,d=x,n
            e,f=n,n
            g,h=n,x
            for t in range(o):
                a1=matrix[a][b]
                a2=matrix[c][d]
                a3=matrix[e][f]
                a4=matrix[g][h]
                matrix[a][b]=a4
                matrix[c][d]=a1
                matrix[e][f]=a2
                matrix[g][h]=a3
                b+=1
                c+=1
                f-=1
                g-=1
            o-=2
            n-=1
