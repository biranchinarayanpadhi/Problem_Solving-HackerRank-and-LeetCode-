class Solution:
    def twoSum(self, a, target):
        maps={}
        count=0
        for i in range(len(a)):
            value=target-a[i]
            if value in maps:
                return [maps[value],i+1]
            else:
                maps[a[i]]=i+1