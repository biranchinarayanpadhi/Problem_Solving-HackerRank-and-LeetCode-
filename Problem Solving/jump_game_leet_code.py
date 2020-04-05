a=[1,0,1,0]
#def jump(a):
#    max_index=0
#    for i in range(0,len(a)):
#        if max_index<i:
#            return False
#        if max_index>=i and i+a[i]>max_index:
#            max_index=i+a[i]
#        print(i,a[i],max_index,)
#    return max_index>=len(a)-1

#jump(a)
    
def jumping(a):
    max_index=0
    i=1
    max_index=a[0]
    while i<len(a) and max_index>=i:
        max_index=max(max_index,i+a[i])
        i+=1
    return max_index>=len(a)-1
        
jumping(a)