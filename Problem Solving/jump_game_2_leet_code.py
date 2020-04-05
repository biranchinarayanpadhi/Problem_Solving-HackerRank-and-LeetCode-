def jump(a):
    if len(a)<2:
        return 0
    count=1
    lim=a[0]
    max_index=a[0]
    for i in range(1,len(a)):
        if i>lim:
            count+=1
            lim=max_index
        max_index=max(max_index,i+a[i])
       
    return count
jump([1,4,2,0,3,1,5,6,7])