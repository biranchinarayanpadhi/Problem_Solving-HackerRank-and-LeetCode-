a=[1,3,2,6,1,2]
count=0
for i in range(len(a)):
    for j in range(len(a)):
        if i<j and (a[i]+a[j])%3==0:
            count+=1
            print('{},{}'.format(a[i],a[j]))

print(count)
            