     def prime_sieve(n): 
        if n<3:
            return 0
        k=[False]*n
        for i in range(3,n,2):
            k[i]=True
        for i in range(3,n,2):
            if(k[i]):
                for j in range(i*i,n,i):
                    k[j]=False
        k[2]=True
        return sum(k)
