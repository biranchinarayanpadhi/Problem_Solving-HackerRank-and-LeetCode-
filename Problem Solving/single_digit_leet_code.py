#import math
a=38
#print(a-9*math.floor((a-1)//9))

def single_digit(a):
    sums=0
    if len(str(a))==1:
        return a
    else:
        for i in str(a):
            sums+=int(i)
#        print(sums)
        return single_digit(sums)

print(single_digit(38))