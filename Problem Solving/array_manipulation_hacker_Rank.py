n=4
operation=[[2,3,603],[1,1,286],[4,4,882]]
a=[0]*(n+1)
for i in range(len(operation)):
    a[operation[i][0]-1]+=operation[i][2]
    if operation[i][1]<=n:
        a[operation[i][1]]-=operation[i][2]

max_value,sums=0,0
for i in a:
        sums=sums+i
        if max_value<sums:
            max_value=sums
print(max_value)