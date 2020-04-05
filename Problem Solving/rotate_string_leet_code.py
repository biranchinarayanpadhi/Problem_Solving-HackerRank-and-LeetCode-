a="abcde"
b="cdeab"
def left_rotate(a,rotate):
    a=list(a)
    li=[]
    i=0
    while i<len(a)-rotate:
        li.append(a.pop(rotate))
    for i in a:
        li.append(i)
    
    return (''.join(i for i in li))



def rotateString(a,b):
    if len(a) and len(b)==0:
        return True
    flag=0
    for i in range(len(a)):
        result=left_rotate(a,i)
        if result==b:
            flag=1
            break
        else:
            flag=0
    
    if flag==1:
        print(True)
    else:
        print(False)
rotateString(a,b)