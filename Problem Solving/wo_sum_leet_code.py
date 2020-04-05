def cal(a,target):
    maps={}
    for i in range(len(a)):
        value=target-a[i]
        if value in maps:
            return maps[value],i
        else:
            maps[a[i]]=i
    
print(cal([3,3],6))                