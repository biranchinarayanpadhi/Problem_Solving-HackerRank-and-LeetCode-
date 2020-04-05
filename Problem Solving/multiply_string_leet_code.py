class Solution(object):
    def convert_to_int(self,num):
        number=0
        length_of_number=len(num)
        for i in num:
            number+=int(i)*(10**(length_of_number-1))
            length_of_number-=1
        return number

    def multiply(self,num1,num2):
        nums1=self.convert_to_int(num1)
        nums2=self.convert_to_int(num2)

        return str(nums1*nums2)
