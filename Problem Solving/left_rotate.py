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


def l_rotate(a,index):
    s=a[index:len(a)]
    print(s)
    s=s+a[:index]
    return s

print(l_rotate("kalia",3))