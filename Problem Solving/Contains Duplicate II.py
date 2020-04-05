class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums)==1:
            return False
        dictis={}
        for i in range(len(nums)):
            if nums[i] in dictis:
                dictis[nums[i]]=abs(dictis[nums[i]]-i)
                if dictis[nums[i]]<=k:
                    return True
            else:
                dictis[nums[i]]=i
        return False
        