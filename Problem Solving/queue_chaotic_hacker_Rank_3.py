def NewYearChaos(q):
    no_of_swaps = 0
    swaped = False

    # checking if the value is chaotic i.e (v-(i+1)) gives the number of swapping 
    # the value V has  i.e either bribed itself or bribed others to reach that position(i.e i)
    #if (v-(i+1)) is positive that means the value V has bribed that many no of elements
    #if (v-(i+1)) is negative that means the Value V is being bribed by someone to change its position
    
    for index, value in enumerate(q):
        if (value- (index+1)) > 2:
            return "Too chaotic"
        
    # after checking the "Too Chaotic condition" just apply bubble sort to count the no of swappings
    for i in range(0,len(q)):
        for j in range(0, len(q)-i-1):
            if q[j] > q[j+1]:
                q[j],q[j+1]=q[j+1],q[j]
                no_of_swaps+= 1
                swaped = True
        
        if swaped:
            swaped = False
        else:
            break
    return no_of_swaps


NewYearChaos([2,5,1,3,4])
