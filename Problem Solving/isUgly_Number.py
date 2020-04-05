def isUgly(nums):
    while nums!=1:
        if nums%2==0:
            nums=nums/2
        elif nums%3==0:
            nums=nums/3
        elif nums%5==0:
            nums=nums/5
        else:
            return False
    return True

isUgly(14)