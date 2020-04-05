def viralAdvertising(n):
    starting=5
    sums=0
    remaining=0
    for i in range(1,n+1):     
        viral=starting//2
        remaining=starting-viral
        sums=sums+viral
        starting=viral*3
        print(remaining,starting,viral)
    return sums

viralAdvertising(5)
    
        