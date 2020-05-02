class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return 
        nums=sorted(nums)
        previous_elem=nums[0]
        length=len(nums)
        i=1
        while i<length:
            if previous_elem == nums[i]:
                return True
            previous_elem=nums[i]
            i+=1    
        return False
            
        