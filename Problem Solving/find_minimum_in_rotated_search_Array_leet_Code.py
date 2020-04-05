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
a=[2,2,2,0,1]
def findMin(a):
    if len(a)==1:
        return a[0]
    
    left,right=0,len(a)-1
    
    while left<right:
       mid=(left+right)//2
       print(left,right,mid)
       if a[mid]>a[right]:
           left=mid+1
       elif a[mid]<a[right]:
           right=mid
       else:
           right-=1
    
    return a[left]
findMin(a)