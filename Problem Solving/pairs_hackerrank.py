def pairs(k, arr):
    count=0
    dicti={}
    for i in range(len(arr)):
        if arr[i] not in dicti:
            dicti[arr[i]]=1
        else:
            dicti[arr[i]]+=1
            
    for i in arr:
        if k+i in dicti:
            print(k+i,i)
            count+=1
    return count
