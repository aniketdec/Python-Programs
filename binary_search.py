def binary_search(ar,x):
    mid=0
    low=0
    high=len(ar)
    flag=0
    while low<=high:
        mid=(low+high)/2
        if ar[mid]==x:
            flag=mid
            break
        else:
            if x<ar[mid]:
                high=mid-1
            else:
                low=mid+1
                
    return flag
