
#Exponential Search : Array should be sorted 
#Time Complexity log(N)
#It is suitable in case of unbounded array (infinite size)

def binarySearch(a,b,c,k):
    l=b
    h=c
    while(l<=h):
        m=(l+h)//2
        if(a[m]==k):
            return m
        elif(a[m]>k):
            h=m-1
        else:
            l=m+1
    return -1

def exponentialSearch(a,k):
    if(a[0]==k):
        return 0
    if(a[0]>k or a[-1]<k):
        return -1
    i=1
    while(i<len(a) and a[i]<=k):
        i=i*2
    return binarySearch(a,i//2,min(i,len(a)-1),k)

print(exponentialSearch([10, 12, 13, 16, 18, 19, 20,21, 22, 23, 24, 33, 35, 42, 47],0))
