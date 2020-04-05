class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num=sorted(nums)
        res=[]
        length=len(num)
        i=0
        dictis={}
        while i<length:
            if num[i] not in dictis:
                dictis[num[i]]=i
            i+=1
        for i in nums:
            res.append(dictis[i])
        return res