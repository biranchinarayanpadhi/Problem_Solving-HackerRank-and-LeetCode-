class Solution(object):
    def addStrings(self, num1, num2):
        nums1=self.convert_to_int(num1)
        nums2=self.convert_to_int(num2)
        return str(nums1+nums2)
    
    def convert_to_int(self,num):
        value = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        result = 0
        for digit in num:
            result = 10 * result + value[digit]
        return result
