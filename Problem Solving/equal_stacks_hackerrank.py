def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    sums1=sum(h1)
    sums2=sum(h2)
    sums3=sum(h3)

    while True:
        mini=min(sums1,sums2,sums3)
        if sums1>mini:
            sums1-=h1.pop(0)
        if sums2>mini:
            sums2-=h2.pop(0)
        if sums3>mini:
            sums3-=h3.pop(0)
        if sums1==sums2==sums3:
            return sums1
