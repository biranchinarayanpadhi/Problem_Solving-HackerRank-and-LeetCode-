def sumXor(n):
    #XOR  does proper decimal addition when it encounters 0 with 1 or 0 with 0 in any 2 numbers. Hence we can count number of zeroes in given number and then we can return 2 to the power of no of zeroes.
    count=0
    while n:
        if n%2 == 0:
            count+=1
        n=n//2
    
    return 2**count
