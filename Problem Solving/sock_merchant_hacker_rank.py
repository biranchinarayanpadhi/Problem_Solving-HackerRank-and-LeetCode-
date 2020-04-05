a=[1,2,1,2,1,3,2]
li={}

def sockMerchant(n,a):
    for i in a:
        li[i]=a.count(i)
    
    count=0
    for i in li:
        if li[i]%2==0 and li[i]>=2:
            count+=li[i]//2
        elif li[i]%2!=0 and li[i]>=2:
            count+=(li[i]-(li[i]%2))//2
        
    return (count)

sockMerchant(10,a)





