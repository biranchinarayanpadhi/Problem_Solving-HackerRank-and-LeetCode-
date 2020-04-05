class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.ps=[]
        sums=0
        for i in nums:
            sums+=i
            self.ps.append(sums)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i==0:
            return self.ps[j]
        else:
            return self.ps[j]-self.ps[i-1] 
