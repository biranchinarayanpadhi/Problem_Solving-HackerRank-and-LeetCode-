b,n,m=input().split()
b=int(b)
n=int(n)
m=int(m)
kb_price=list(map(int,input().split()))
usb_price=list(map(int,input().split()))

def getMoneySpent(kb_price,usb_price,b):
    li=[]
    for key_board in kb_price:
        for usb in usb_price:
            if key_board+usb<=b:
                li.append(key_board+usb)
    if len(li)>0:
        return max(li)
    else:
        return -1        
    