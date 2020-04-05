a="Hi"
b="world"
dictis={}
count=0
for i in a:
    if i in dictis:
        dictis[i]+=1
    else:
        dictis[i]=0
for j in b:
    if j in dictis:
        count+=1
if count==0:
    return "No"
else:
    return "Yes"
    