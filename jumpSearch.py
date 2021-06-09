#time complexity O((n)^(1/2))
import math
def jumpSearch(arr,k):
    m=int(math.sqrt(len(arr)))
    temp=0
    for i in range(0,len(arr),m-1):
        if(arr[i]>k):
            break
    temp=i-1
    while(arr[temp]<=k and temp<len(arr)):
        if(arr[temp]==k):
            return temp
        temp+=1
    return -1

print(jumpSearch([0, 1, 1, 2, 3, 5, 8, 13, 21,34, 55, 89, 144, 233, 377,378, 610],610))

