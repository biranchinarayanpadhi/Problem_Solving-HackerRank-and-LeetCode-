class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        if length == 1:
            return
        if k == 0:
            return
        k=k%length
        i=0
        j=length-1
        while i<=j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        position=(k-1)
        i=0
        while i<=position:
            nums[i],nums[position]=nums[position],nums[i]
            i+=1
            position-=1
        
        position=k
        j=length-1
        while position<=j:
            nums[position],nums[j]=nums[j],nums[position]
            j-=1
            position+=1
        
        
        
        