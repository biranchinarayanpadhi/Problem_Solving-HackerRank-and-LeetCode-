class s_linklist(object):
    def __init__(self,value):
        self.value=value
        self.next=None
        
a=s_linklist(1)
b=s_linklist(2)
c=s_linklist(3)
d=s_linklist(4)

a.next=b
b.next=c
c.next=d

print(a.value,a.next.value)
print(b.value,b.next.value)
print(c.value,c.next.value)
print(d.value,d.next)


def printReverse(head):
    if head==None:
        return
    
    printReverse(head.next)
    
    print(head.value)
    
print(printReverse(a))