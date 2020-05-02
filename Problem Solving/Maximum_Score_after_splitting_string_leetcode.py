class Solution:
    def maxScore(self, s: str) -> int:
        
        max_score=0
        left_dicti={}
        right_dicti={}
        
        left_dicti["0"]=0
        left_dicti["1"]=0
        right_dicti["0"]=0
        right_dicti["1"]=0
        
        left_dicti[s[0]]+=1
        
        
        for index in range(1,len(s)):
            right_dicti[s[index]]+=1       
            
        print(right_dicti)
        
   
        max_score=max(max_score,left_dicti["0"]+right_dicti["1"])
        
        for index in range(1,len(s)-1):
            ele=s[index]
            left_dicti[ele]+=1  
            right_dicti[ele]-=1
                     
            max_score=max(max_score,left_dicti["0"]+right_dicti["1"])
                      
        return max_score
                
       