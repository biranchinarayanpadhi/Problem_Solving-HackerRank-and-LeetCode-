class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dicti={}
        k=i=count=0
        length=len(nums)
        while i<length:
            if nums[i] not in dicti:
                dicti[nums[i]]=0
                nums[k]=nums[i]
                count+=1
                k+=1
            i+=1
        print(count)
        return count
            
        