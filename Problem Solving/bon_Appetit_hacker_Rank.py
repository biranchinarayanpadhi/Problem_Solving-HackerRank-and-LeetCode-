def bonAppetit(bill, k, b):
    bill.pop(k)
    total=sum(bill)/2
    if total==b:
        return "Bon Appetit"
    else:
        return int(abs(b-total))

bill=[3,10,2,9]
k=1
b=7

bonAppetit(bill,k,b)