a=[2,2,5,5,5,1,9]
a=[1,2,2,3]
a=[3,3,2,1,3]

dict={}
for i in a:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1

print(sum(dict.values())-max(dict.values()))

