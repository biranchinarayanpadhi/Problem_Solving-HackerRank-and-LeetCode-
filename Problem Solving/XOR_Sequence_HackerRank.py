def XOR(number):
    remainder=number%8
    if remainder ==0 or remainder == 1:
        return number
    elif remainder == 6 or remainder == 7:
        return 0
    elif remainder == 4 or remainder == 5:
        return number+2
    else:
        return 2

def xorSequence(l, r):
    #here the logic is based upon L^R=(A[1]^A[2]^...A[R])^(A[1],A[2]...A[L-1]) as a^a=0 and 0^a=a and the XOR function logic is based upon the observations from the sample test cases, it worked fine for me
    return XOR(l-1)^XOR(r)
