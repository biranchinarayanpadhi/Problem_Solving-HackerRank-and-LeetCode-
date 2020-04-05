a="1232"
b="2123"

def convert_to_int(num):
    value = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    result = 0
    for digit in num:
        result = 10 * result + value[digit]
    return result

def multiply(num1,num2):
    nums1=convert_to_int(num1)
    nums2=convert_to_int(num2)
    
    return str(nums1*nums2)

multiply(a,b)
        