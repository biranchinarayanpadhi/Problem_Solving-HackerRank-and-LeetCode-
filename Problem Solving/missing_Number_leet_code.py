#Approach 1
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        expected_sum=(n*(n+1))//2
        return expected_sum-sum(nums)
 
#Approach 2:
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map={}
        length_nums=len(nums)
        for index in range(length_nums):
            element=nums[index]
            if element not in hash_map:
                hash_map[element]=1
        
        for number in range(length_nums+1):
            if number not in hash_map:
                return number

#Approach 3:
class Solution:
    def missingNumber(self, a):
        a=sorted(a)
        for i in range(0,len(a)+1):
            if i not in a:
                return i
