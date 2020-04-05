def paliandrome(a):
    rev=0
    while(a!=0):
        rev=rev*10+a%10
        print(rev)
        a=a//10
    return rev
    
def reverse(x):
    if x>=0:
       return paliandrome(x)
    else:
        x=int(str(x)[1:len(str(x))])
        x=paliandrome(x)
        x='-'+str(x)
        x=int(x)
        return x
    
paliandrome(-123)
        
