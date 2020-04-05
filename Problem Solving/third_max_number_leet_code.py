class Solution(object):
    def thirdMax(self, nums):
        unique_list=list(set(nums))
        desc_ord_list=sorted(unique_list,reverse=True)
        if len(desc_ord_list)==1:
            return desc_ord_list[0]
        if len(desc_ord_list)==2:
            return unique_list[1]
        else:
            return desc_ord_list[2]
            
            