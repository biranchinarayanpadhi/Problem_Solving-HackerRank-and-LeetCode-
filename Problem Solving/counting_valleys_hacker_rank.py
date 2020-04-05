n=int(input())
s=input()
a='DDUUUUDD'

def countingValleys(n,s):
    count=0
    mountain=0
    valley=0
    for i in s:
        if i=='U':
            count+=1
            if count==1:
                mountain+=1
        else:
            count-=1
            if count==-1:
                    valley+=1
    return valley

countingValleys(n,a)