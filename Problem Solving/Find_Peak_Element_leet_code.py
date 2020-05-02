class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        if length == 1:
            return 0
        return self.peakIndex(nums,0,length-1)
    
    def peakIndex(self,nums,left,right):
        if left<=right:
            mid=(left+right)//2

            if mid == 0:
                if nums[mid]>nums[mid+1]:
                    return mid
                else:
                    return self.peakIndex(nums,mid+1,right)
            if mid == len(nums)-1:
                if nums[mid]>nums[mid-1]:
                    return mid
            if nums[mid]<nums[mid-1]:
                return self.peakIndex(nums,left,mid)
            elif nums[mid]<nums[mid+1]:
                return self.peakIndex(nums,mid+1,right)
            else:
                return mid
        else:
            return 