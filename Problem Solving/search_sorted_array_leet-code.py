a=[7,0,0,1,2,4,5,6]

def search(a,target,left,right):
    if not a:
        return -1
    
    while left<=right:
        mid=(left+right)//2
        
        if target==a[mid]:
            return mid
        
        elif a[left]<=a[mid]:
            if target>=a[left] and target<=a[mid]:
                right=mid-1
            else:
                left=mid+1
            
        else:
            if target<=a[right] and target>=a[mid]:
                left=mid+1
            else:
                right=mid-1
    else:
        return -1

search(a,0,0,6)