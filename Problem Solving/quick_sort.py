def quicksort(a,low,high):
#    print(low,high)
    if(high>low):
        pivot=partition(a,low,high)
        print(pivot)
        quicksort(a,low,pivot-1)
        quicksort(a,pivot+1,high)


def partition(a,low,high):
    left=low
    right=high
    pivot=a[low]
#    while left<right:
#        while(a[left]<=pivot):
#            left+=1
#        while a[right]>pivot:
#            right-=1
#        if left<right:
#            temp=a[left]
#            a[left]=a[right]
#            a[right]=temp
#    a[low]=a[right]
#    a[right]=pivot
#    return right
    while left<right:
        while a[left]<=pivot:
            left+=1
        while a[right]>pivot:
            right-=1
        if left<right:
            temp=a[left]
            a[left]=a[right]
            a[right]=temp
    a[low]=a[right]
    a[right]=pivot
    return right

def main():
    li=[15,3,2,10,99999]
    quicksort(li,0,len(li)-1)
    print(li)

if __name__=='__main__':
    main()