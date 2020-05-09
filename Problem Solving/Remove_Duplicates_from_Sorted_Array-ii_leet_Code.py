class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        length_nums=len(nums)
        dicti={}
        for index in range(length_nums):
            element=nums[index]
            if element not in dicti:
                dicti[element]=1
            else:
                dicti[element]+=1
        
        temp_dicti={}
        index=0
        while index<length_nums:
            element=nums[index]
            if element not in temp_dicti:
                if dicti[element]>=2:
                    nums[k]=element
                    nums[k+1]=element
                    k+=2
                    index+=dicti[element]
                else:
                    nums[k]=element
                    k+=1
                    index+=dicti[element]
            else:
                temp_dicti[element]=0
        return k