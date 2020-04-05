a=[1,2,1,2,3]
b=list(set(a))
for i in b:
    if a.count(i)==1:
        print(i)
    else:
        continue
    
#another_logic
dicti={}
for i in a:
    if i in dicti:
        dicti[i]+=1
    else:
        dicti[i]=1

for k,v in dicti.items():
    if v==1:
        print(k)
        break;

#another logic
dictis={}
for i in a:
    if i in dictis:
        del dictis[i]
    else:
        dictis[i]=1
    
for i in dictis:
    i