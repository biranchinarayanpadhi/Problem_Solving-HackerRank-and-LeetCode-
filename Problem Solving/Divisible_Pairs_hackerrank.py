#Brute Force Approach (Accepted-O(N*N)):
	def divisibleSumPairs(n, k, a):
    count=0
    for i in range(len(a)):
        for j in range(len(a)):
             if i<j and (a[i]+a[j])%k==0:
                count+=1
    return count

#Optimized Approach(Accepted-O(N))
def divisibleSumPairs(n, k, a):
    count=0
    dicti={}
    for index in range(n):
        element=a[index]
        if element%k not in dicti:
            dicti[element%k]=[index]
        else:
            dicti[element%k].append(index)
    
    if 0 in dicti:
        n=len(dicti[0])
        count+=(n*(n-1))//2

    for element in a:
        rem=element%k
        if rem != 0 and k-rem in dicti:
            original_index=dicti[rem].pop(0)
            for greater_index in dicti[k-rem]:
                if original_index<greater_index:
                    count+=1
    return count
