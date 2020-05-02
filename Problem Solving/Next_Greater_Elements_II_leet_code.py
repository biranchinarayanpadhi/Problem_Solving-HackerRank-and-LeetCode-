class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        dicti={}
        stack=[]
        length=len(nums)
        index=0
        result=[]
        
        if length == 0:
            return []
        elif length == 1:
            return [-1]
        else:
            while index<length:
                nums.append(nums[index])
                index+=1

            new_length=len(nums)
            stack.append(nums[0])
            for index in range(1,new_length):
                if stack:
                    ele=stack.pop()
                    while ele<nums[index]:
                        if ele in dicti:
                            dicti[ele].append(nums[index])
                        else:
                            dicti[ele]=[nums[index]]

                        if len(stack) == 0:
                            break

                        ele=stack.pop()

                    if ele>=nums[index]:
                        stack.append(ele)

                stack.append(nums[index])

            while stack:
                ele=stack.pop()
                if ele not in dicti:
                    dicti[ele]=[-1]
                else:
                    dicti[ele].append(-1)

            temp_dicti={}
            for index in range(length):
                ele=nums[index]
                if ele not in temp_dicti:
                    temp_dicti[ele]=0
                    result.append(dicti[ele][0])
                else:
                    temp_dicti[ele]+=1
                    result.append(dicti[ele][temp_dicti[ele]])

            return result
