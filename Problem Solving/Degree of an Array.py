class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_dictis={}
        index_dictis={}
        diffindex_dictis={}
        length=len(nums)
        
        if length==1:
            return length
        
        for i in range(length):
            element=nums[i]
            if element in count_dictis:
                count_dictis[element]+=1
                diffindex_dictis[element]=abs(index_dictis[element]-i)
            else:
                count_dictis[element]=1
                diffindex_dictis[element]=i
                index_dictis[element]=i
        
        maxi=max(count_dictis.values())
        small=length
                
        for i in count_dictis:
            if maxi==count_dictis[i] and small>diffindex_dictis[i]:
                small=diffindex_dictis[i]
        return small+1
       