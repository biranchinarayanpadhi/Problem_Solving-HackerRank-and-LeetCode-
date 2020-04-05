class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictis={}
        for i in nums:
            if i in dictis:
                return True
            else:
                dictis[i]=0
        return False