class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length=len(nums)
        nums1=sorted(nums)
        element_tobe_searched=0
        dicti={}
        for index in range(length):
            if nums[index] not in dicti:
                dicti[nums[index]]=[index]
            else:
                dicti[nums[index]].append(index)
        
        for i in range(0,length):
            element_tobe_searched=target-nums1[i]
            if nums1[i] == element_tobe_searched:
                returned_result=self.binarySearch(nums1,0,length-1,element_tobe_searched)
                print(returned_result,i,nums[i],element_tobe_searched)
            
                if returned_result != -1:
                    return [dicti[nums1[i]][0],dicti[nums1[i]][1]]
            else:
                returned_result=self.binarySearch(nums1,0,length-1,element_tobe_searched)
                print(returned_result,i,nums[i],element_tobe_searched)
            
                if returned_result != -1:
                    return [dicti[nums1[i]][0],dicti[element_tobe_searched][0]]
  
    def binarySearch(self,nums,left,right,element_tobe_searched):
        
        if right>=left:
            mid=(left+right)//2
            
            if nums[mid] == element_tobe_searched:
                return mid
            elif nums[mid]<element_tobe_searched:
                return self.binarySearch(nums,mid+1,right,element_tobe_searched)
            else:
                return self.binarySearch(nums,left,mid-1,element_tobe_searched)
        else:
            return -1
  
