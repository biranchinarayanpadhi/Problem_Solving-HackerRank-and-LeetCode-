def utopianTree(n):
    li=[]
    for i in range(n+1):
        print(i)
        if i==0:
            li.append(1)
        else:
            if i%2==0:
                previous=li[i-1]+1
                li.append(previous)
            else:
                li.append(2*li[i-1])
    return li[n]


