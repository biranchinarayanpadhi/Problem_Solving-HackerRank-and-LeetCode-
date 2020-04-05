#O(n) Solution
#----------------------
#a=[3,4,5,1,2]
#mini=a[0]
#for i in a:
#    if mini>i:
#        mini=i
#print(mini)

#O(log n) solution
#----------------------------
a=[4,5,6,7,0,1,2]
def findMin(a):
    if len(a)==1:
        return a[0]
    
    left,right=0,len(a)-1
    if a[right]>a[0]:
        return a[0]
    
    while left<=right:
           mid=(left+right)//2
 
        if a[mid]>a[mid+1]:
            return a[mid+1]
        elif a[mid-1]>a[mid]:
            return a[mid]
        
        if a[mid]>a[0]:
            left=mid+1
        else:
            right=mid-1
    else:
        return -1

findMin(a)