class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        large=0
        index=0
        length=len(nums)
        for i in range(length):
            if large<nums[i]:
                large=nums[i]
                index=i
        
        for i in nums:
            if not i*2<=large and i!=large:
                    return -1
        return index