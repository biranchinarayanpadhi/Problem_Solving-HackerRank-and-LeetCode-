a=["a","b","c"]
i=0
rotate=2
li=[]
while(i<rotate):
    print(i)
    li.append(a.pop(len(a)-1))
    i+=1

li=list(reversed(li))

for i in a:
    li.append(i)
print(li)

#another logic without reversing the array
a=[1,2,3,4,5]

rotate=10
li=[]
i=rotate
while i<len(a):
    li.append(a[i])
    i+=1
for i in range(rotate):
    li.append(a[i])
print(li)
    

