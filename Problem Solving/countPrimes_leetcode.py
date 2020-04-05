def countPrimes(n):
        if n<2:
         return 0
        a=[1]*(n-1)
        for i in range(2,n):
            if a[i-1]==1:
                k=i*i
                while k<n:
                    print(k)
                    a[k-1]=0
                    k+=i
        return a.count(1)-1
    
countPrimes(3)