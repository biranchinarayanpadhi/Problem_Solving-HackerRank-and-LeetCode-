class Solution(object):
    def pivotIndex(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums=k=0
        length=len(arr)
        if length==0:
            return -1
        ps=[0]*length
        for i in arr:
            sums+=i
            ps[k]=sums
            k+=1

        #print(ps)   

        lsum=0
        rsum=ps[length-1]-ps[0]
        if lsum==rsum:
            return 0
   
        i=1    
        while i<len(arr)-1:
            lsum=ps[i]-arr[i]
            rsum=ps[length-1]-ps[i]
            if lsum==rsum:
                return i
            i+=1
            
        lsum=ps[length-1]-arr[length-1]
        rsum=0
        if lsum==rsum:
            return length-1
        
        return -1