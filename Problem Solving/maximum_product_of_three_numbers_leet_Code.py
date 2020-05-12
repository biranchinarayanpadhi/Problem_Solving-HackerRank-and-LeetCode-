#Brute Force Approach (O(NlogN))

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        #Brute Force Appraoch
     #   products=[]
      #  len_nums=len(nums)
       # for i in range(len_nums):
        #    for j in range(i+1,len_nums):
         #       for k in range(j+1,len_nums):
          #          products.append(nums[i]*nums[j]*nums[k])
        #return max(products)
    
        #bit improvised Solution
        nums.sort()
        len_nums=len(nums)
        if len_nums == 3:
            return nums[0]*nums[1]*nums[2]
        else:
            if nums[len(nums)-1]<0:
                return nums[len_nums-1]*nums[len_nums-2]*nums[len_nums-3]
            else:
                count_positive=0
                count_negative=0
                end=len_nums-1
                start=0
                while start<end:
                    if nums[start]>0:
                        count_positive+=1
                    if nums[end]>0:
                        count_positive+=1
                    if nums[start]<0:
                        count_negative+=1
                    if nums[end]<0:
                        count_negative+=1
                    
                    if count_negative == 2:
                        break
                    start+=1
                    end-=1
                if start == end:
                    if start>0:
                        count_positive+=1
                    else:
                        count_negative+=1
                
                print(count_positive,count_negative)
                
                if count_negative>=2:
                    
                    if nums[0]*nums[1]*nums[-1] > nums[-1]*nums[-2]*nums[-3]:
                        return nums[0]*nums[1]*nums[-1]
                    else:
                        return nums[-1]*nums[-2]*nums[-3]
                
                if count_positive == 1:
                    return nums[-1]*nums[0]*nums[1]
                
                if count_positive>=2:
                    return nums[-1]*nums[-2]*nums[-3]
                        

#Approach 2(Bit Optimized and clean Code in O(NlogN)):
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3])
 
#Fully Optimized Version(O(N)):
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length_nums=len(nums)
        
        #here i have intialized -1001 because it -1000 is the min value as given in the constraint so my maximum will be always greater than or equal to -1001

        maxi1=-1001
        maxi2=-1001
        maxi3=-1001
        
        #here i have intialized 1001 because it 1000 is the max value as given in the constraint so my minimum will be always less than or equal to 1000
        mini1=1001
        mini2=1001  
       
        #finding the 2 minimum value and 3 maximum value from array 
        for index in range(length_nums):
            element=nums[index]
            if element>=maxi1:
                maxi3=maxi2
                maxi2=maxi1
                maxi1=element
                
            elif element!=maxi1 and element>=maxi2:
                maxi3=maxi2
                maxi2=element
                
            elif element!=maxi1 and element!=maxi2 and element>=maxi3:
                maxi3=element
                
            if element <=mini1:
                mini2=mini1
                mini1=element
                
            elif element!=mini1 and element<=mini2:
                mini2=element
        
        return max(mini1*mini2*maxi1,maxi1*maxi2*maxi3)
       
        
     