class Solution(object):
    def findMin(self, a):
        """
        :type nums: List[int]
        :rtype: int
        """
        length_a=len(a)
        if length_a == 1:
            return a[0]
        
        if a[0]<a[length_a-1]:
            return a[0]
        
        left=0
        right=length_a-1
        
        while left<=right:
            
            mid=(left+right)//2
            
            if a[mid]>a[mid+1]:
                return a[mid+1]
            if a[mid-1]>a[mid]:
                return a[mid]
            if a[mid]>a[0]:
                left=mid+1
            else:
                right=mid-1
        else:
            return -1
        
                