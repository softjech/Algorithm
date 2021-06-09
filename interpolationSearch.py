
#Interpolation Search is for array i.e uniformly distributed and sorted
#Formula low + ((key-arr[low])/(arr[high]-arr[low]))*(high-low)
def interpolationSearch(arr,k):
    l=0
    h=len(arr)-1
    while(l<=h and arr[l]<=k and arr[h]>=k):
        pos= l+((k-arr[l])*(h-l))//(arr[h]-arr[l])
        if(arr[pos]==k):
            return pos
        elif(arr[pos]>k):
            l=pos+1
        else:
            h=pos-1
    return -1

print(interpolationSearch([1,3,5,7,9,11,13,15],15))
