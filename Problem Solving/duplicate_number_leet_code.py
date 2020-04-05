def duplicateNumber(a):
    dictis={}
    n=len(a)
    for i in range(0,n):
        if a[i] in dictis:
            return a[i]
        else:
            dictis[a[i]]=0

duplicateNumber([-93,86,49,-62,-90,-63,40,72,11,67])
        