def kaprekarNumbers(p, q):
    count=0
    if p==1:
        print(p,end=" ")
        p+=1
        count+=1
    while p<=q:
        if 2<=p<=3:
            p+=1
            continue
        elif 4<=p<=9:
            square_string=str(p**2)
            left=int(square_string[:1])
            right=int(square_string[1:])
            if left+right == p:
                print(p,end=" ")
                count+=1
        else:
            square_string=str(p**2)
            d=int(math.log10(p))+1
            square_len=len(square_string)
            left=square_string[:square_len-d]
            right=square_string[square_len-d:]
            if int(left)+int(right) == p:
                print(p,end=" ")
                count+=1
        p+=1
    
    if count == 0:
        print("INVALID RANGE")
