def diff_diagonals(arr):
    sums=0    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i==j:
                print(arr[i][j])
                sums=sums+arr[i][j]
    
    
    kal=0
    j=0
    for i in reversed(range(len(arr))):
        print(arr[j][i])
        kal=kal+arr[j][i]
        j=j+1
    
    diff=abs(sums-kal)
    print(diff)        
