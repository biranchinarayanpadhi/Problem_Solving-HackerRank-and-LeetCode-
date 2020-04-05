a=[1,2,3,4,5]

def product_array(a):
    product=1
    for i in a:
        product=product*i
    
    for i in range(len(a)):
        a[i]=product//a[i]
    return a

product_array(a)
        