a=[4,3,1,2]
count=0
i=0
#for i in range(len(a)):
while i<(len(a)):
    if a[i]==a[a[i]-1]:
        i+=1
        continue
    if a[i]!=a[a[i]-1]:
        temp=a[i]
        a[i]=a[a[i]-1]
        a[temp-1]=temp
        count+=1
#        print(a)
#        break
        
print(count)