a=[1,2,3,3,3,4,5]
li=list(set(a))
flag=1
for i in li:
    if a.count(i) >=len(a)//2:
        flag=0
        print(i)
        break
    
if flag==1:
   print("-1") 