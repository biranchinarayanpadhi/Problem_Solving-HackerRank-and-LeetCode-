m=int(input())
li=list(map(int,input().split()))

def migratory_birds(li):
    dic={i:li.count(i) for i in li}
    
    for i in li:
        
        dic[i]=li.count(i)
        
    print(dic)
    
    k={}
    for i in dic:
       if max(dic.values())==dic[i]:
           k[i]=max(dic.values())
    
    return (min(k.keys())) 

return (migratory_birds(li)  
       
