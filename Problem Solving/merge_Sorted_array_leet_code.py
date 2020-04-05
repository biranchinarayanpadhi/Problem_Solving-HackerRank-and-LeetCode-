#def merge(nums1, m, nums2, n):
#    """
#    :type nums1: List[int]
#    :type m: int
#    :type nums2: List[int]
#    :type n: int
#    :rtype: void Do not return anything, modify nums1 in-place instead.
#    """
#    temp=m
#    i=0
#    while(i<n):
#        nums1[temp]=nums2[i]
#        i+=1
#        temp+=1
#    nums1.sort()
#    print(nums1)
#        
#
#merge([1,2,3,0,0,0],3,[2,5,6],3)

def merge(nums1, m, nums2, n):
    i = j = 0
    while j < n:
        if i >= m + j or nums1[i] >= nums2[j]:
            nums1.insert(i, nums2[j])
            print(nums1)
            j += 1
        i += 1
    
    while len(nums1) > m + n:
        nums1.pop()
merge([1,2,3,0,0,0],3,[2,5,6],3)