n=int(input())
a=list(map(int,input().split()))

d,m=input().split()

def birthday(a,d,m):
    count,i,j,sums=0,0,0,0
    while(i<=len(a)-int(m)):
        ranges=i+int(m)
        while j!=ranges:
#            print(j)
            sums+=a[j]
            j+=1
        if sums==int(d):
#            print(a[i],a[j])
            count+=1
        sums=0
        j=i+1
        i+=1
        
    print(count)
birthday(a,d,m)