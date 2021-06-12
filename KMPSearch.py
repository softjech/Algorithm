#Time Complexity O(N)
def LongestPrefixSuffix(s,lps):
    l=0 # length of the logest prefix suffix
    m=len(s)
    i=1
    while(i<m):
        if(s[i]==s[l]):
            l+=1
            lps[i]=l
            i+=1
        else:
            if(l!=0):
                l=lps[l-1]
            else:
                lps[i]=0
                i+=1
def KMPSearch(p,t):
    a=len(t)
    b=len(p)
    lps=[0]*b
    LongestPrefixSuffix(p,lps)
    j=0 #index for pattern
    i=0 #index for text
    while(i<a):

        if(p[j]==t[i]):
            i+=1
            j+=1
        if(j==b):
            print(f"Found patter at {i-j}")
            j=lps[j-1]
        elif (i<a and p[j]!=t[i]):
            if(j!=0):
                j=lps[j-1]
            else:
                i+=1


txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)
