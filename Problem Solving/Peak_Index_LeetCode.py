class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        length=len(A)
        return self.peakIndex(A,0,length-1)
    
    def peakIndex(self,nums,left,right):
        
        if right>=left:
            
            mid=(left+right)//2
            if nums[mid-1]< nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid-1]< nums[mid] <nums[mid+1]:
                return self.peakIndex(nums,mid+1,right)
            else:
                return self.peakIndex(nums,left,mid-1)