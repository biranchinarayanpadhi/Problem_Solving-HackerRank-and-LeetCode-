a=[1,1,2,3,4,3,4,5,2,2]

for i in range(1,len(a)): 
    hole=i
    value=a[i]
    while(hole>0 and a[hole-1]>value):
        a[hole]=a[hole-1]
        hole-=1
    a[hole]=value

print(a)
        
       