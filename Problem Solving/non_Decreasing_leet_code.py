#a=[1,5,4,6,7,10,8,9]
#a=[3,3,2,2]
#a=[4,2,3]
#a=[4,2,1]
#a=[3,4,2,3]
def non_decreasing(a):
    count=0
    for i in range(len(a)-1):
        if not a[i]<=a[i+1]:
            count+=1
            for j in range(i):
                if a[j]>=a[i+1]:
                    return False
    if count==0 or count==1:
        return True 
    else:
        return False
non_decreasing(a)        