class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter_dicti={}
        for character in s:
            if character not in counter_dicti:
                counter_dicti[character]=1
            else:
                counter_dicti[character]+=1
                
        for character in t:
            if character not in counter_dicti:
                return character
            else:
                counter_dicti[character]-=1
                if counter_dicti[character]<0:
                    return character
          
