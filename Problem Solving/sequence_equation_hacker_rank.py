a=[2,3,1]
dictis={}
for i in range(len(a)):
    dictis[i+1]=a[i]
li=[]
for i in range(len(a)):
    for key,value in dictis.items():
        if i+1==value:
            val=key
            for keys,values in dictis.items():
                if val==values:
                    li.append(keys)
                    break;
print(li)