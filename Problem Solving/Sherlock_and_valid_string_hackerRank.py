def isValid(s):
    dicti={}
    counting_dicti={}
    if len(s) ==1 :
        return "YES"
    for i in s:
        if i not in dicti:
            dicti[i]=1
        else:
            dicti[i]+=1
    
    arr=list(dicti.values())
    print(arr)
    elem=arr[0]
    count=0
    diff_elem=0
    for i in arr:
        if i  != elem:
            diff_elem=i
            count+=1
    
    if count == 1:
        if (diff_elem-1) == elem or (diff_elem-1) == 0:
            return "YES"
        else:
            return "NO"
    elif count ==0 :
        return "YES"
    else:
        return "NO"
