class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo={}
        memo[1]=1
        memo[2]=2
        if n<=2:
            return memo[n] 
        
        number=3
        while number<=n:
            memo[number]=memo[number-2]+memo[number-1]
            number+=1
            
        return memo[n]