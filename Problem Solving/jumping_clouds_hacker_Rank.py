
a=[0,0,0,0,1,0,0,1,0]
n=len(a)
count=0
i=0
while i<len(a):
    if i==n-1:
        print(count)
        break
    if i==n-2:
        i+=1
        count+=1
        print(count)
        break
    elif a[i+2]==0:
        i=i+2
        count+=1
    elif a[i+1]==0:
        i=i+1
        count+=1
    
    
        