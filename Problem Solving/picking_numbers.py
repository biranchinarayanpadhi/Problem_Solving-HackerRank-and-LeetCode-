a=[1,2,2,3,1,2]
li=[]
a=sorted(a)
for i in range(len(a)):
    b=[]
    b.append(a[i])
    for j in range(i+1,len(a)):
        if abs(a[i]-a[j]) <= 1:
            b.append(a[j])
    print(b)
    li.append(len(b))
print(max(li))

    