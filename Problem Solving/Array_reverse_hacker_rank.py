def reverseArray(a):
    i=len(a)-1
    strs=""
    while i>=0:
        strs=strs+str(a[i])+" "
        i-=1
    strs=strs.strip()
    return strs

print(" ".join(reversed([54,4,3,6762])))
#reverseArray([54,4,3,6762])