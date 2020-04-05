a=[1,1,1,2,2,3,3,4]
j=0
for i in range(len(a)-1):
    if a[i]!=a[i+1]:
        a[j]=a[i]
        j+=1
a[j]=a[len(a)-1]
j+=1
a=a[0:j]
print(a)