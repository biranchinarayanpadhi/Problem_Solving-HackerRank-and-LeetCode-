a=["hahshs","ccc","as","hah"]
b=["hahshs"]
def halindrome(s):
    count=0
    if len(s)>=2 and paliandrome(s):
        count+=1
#        print(count)
        return count
    elif len(s)%2==0 and len(s)>=2:
        mid=len(s)//2
        s1=s[0:mid]
        s2=s[mid:len(s)]
#        print(s1)
#        print(s2)
        res=halindrome(s1)
        res=res+halindrome(s2)
        if res>=1:
            return 1
    elif len(s)%2!=0 and len(s)>=2:
        mid=len(s)//2
        s1=s[0:mid]
        s2=s[mid+1:len(s)]
        res=halindrome(s1)
        res=res+halindrome(s2)
        if res>=1:
            return 1
    else:
        count=count
    return count

def paliandrome(s):
    if s[::-1]==s:
        return True
    else:
        return False

sums=0    
for string in a:
    response=halindrome(string)
#    print(response)
    if response>=1:
        sums+=1
print(sums)    