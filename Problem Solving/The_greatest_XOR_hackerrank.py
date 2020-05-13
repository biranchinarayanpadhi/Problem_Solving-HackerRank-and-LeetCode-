def theGreatXor(x):
    count=0
    copy_of_x=x
    while x:
        count+=1
        x=x//2
    return (2**count)-copy_of_x-1
