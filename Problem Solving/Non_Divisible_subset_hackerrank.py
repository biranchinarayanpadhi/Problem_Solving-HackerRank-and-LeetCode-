#Brute Force Approach(TLE-TIME LIMIT EXCEEDED):
def nonDivisibleSubset(k, s):
    # Write your code here
    temp_dicti={}
    count=0
    maximum=0
    nums=[]
    length_s=len(s)
    for i in range(length_s):
        nums.append(s[i])
        for j in range(length_s):
            flag=0
            if i != j:
                for number in nums:
                    if (s[j]+number)%k==0:
                        flag=1
                if flag!=1:
                    count+=1
                    nums.append(s[j])
        maximum=max(count+1,maximum)
        if maximum == length_s:
            return maximum
        count=0
        del nums
        nums=[]
    return maximum

#Optimized Version one using DefaultDict:
def nonDivisibleSubset(k, s):
    # Write your code here
    remainder_dicti=defaultdict(int)
    count=0
    for number in s:
        rem=number%k
        if rem not in remainder_dicti:
            remainder_dicti[rem]=1
        else:
            remainder_dicti[rem]+=1
    if k%2==0:
        remainder_dicti[k//2]=min(1,remainder_dicti[k//2])
        
    for rem in range((k//2)+1):
        if rem==0:
            count+=min(1,remainder_dicti[rem])
        else:
            count+=max(remainder_dicti[rem],remainder_dicti[k-rem])
    
    return count

#Optimized Version clean code:
def nonDivisibleSubset(k, s):
    # Write your code here

    #Hint is two number which gives is divisible by k, their sum of remainder is K. 
    remainder_frequency_array=[0]*k
    for number in s:
        remainder_frequency_array[number%k]+=1

    if k%2==0:
        remainder_frequency_array[k//2]=min(remainder_frequency_array[k//2],1)
    
    count=min(remainder_frequency_array[0],1)
    for remainder in range(1,(k//2)+1):
        count+=max(remainder_frequency_array[remainder],remainder_frequency_array[k-remainder])
    
    return count
