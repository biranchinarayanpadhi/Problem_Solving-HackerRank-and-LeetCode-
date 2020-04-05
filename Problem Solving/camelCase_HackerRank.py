def camelcase(s):
    count=0
    for i in s:
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            count+=1
    return count+1