a=[1,9,5,2,6,1,4]

k=4
running_sum=0
for i in range(0,k):
    running_sum+=a[i]
print(running_sum)
i=0
j=k
while j<len(a) and i<j:
    running_sum=running_sum-a[i]+a[j]
    print(running_sum)
    i+=1
    j+=1
    




















