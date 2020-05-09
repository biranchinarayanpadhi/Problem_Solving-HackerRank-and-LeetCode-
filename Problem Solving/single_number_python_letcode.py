#Approach 1:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        XOR=nums[0]
        for index in range(1,len(nums)):
            number=nums[index]
            XOR^=number
        return XOR

#Approach 2:
class Solution:
    def singleNumber(self, a):
        dictis={}
        for i in a:
            if i in dictis:
                dictis[i]+=1
            else:
                dictis[i]=1
    
        for i in dictis:
            if dictis[i]==1:
                return i