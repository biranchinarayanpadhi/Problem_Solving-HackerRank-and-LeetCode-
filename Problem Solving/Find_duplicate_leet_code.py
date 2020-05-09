#Most Optimized Approach
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #Here i am finding the intersection point of slow and fast
        fast=slow=nums[0]
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow == fast:
                break
        
        #Here i am detecting from which point the cycle began and that is my answer
        slow=nums[0]
        while slow !=fast:
            slow=nums[slow]
            fast=nums[fast]
        
        return slow

#Approach 2:
class Solution:
    def findDuplicate(self, a):
        dictis={}
        n=len(a)+1
        for i in range(0,n):
            if a[i] in dictis:
                return a[i]
            else:
                dictis[a[i]]=0
