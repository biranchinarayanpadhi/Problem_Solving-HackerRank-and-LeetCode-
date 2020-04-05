a=[1,1,1,0,1,1,0,0,0,0]
k=3
n=len(a)
i=(0+k)%n
e=100
while i<len(a):
    if a[i]==1:
        e=e-2
    e=e-1
    if i==0:
        print(e)
        break
    i=(i+k)%n
    if i==n-1:
        if a[i]==1:
            e=e-2
        e=e-1
        i=0
    print(i)