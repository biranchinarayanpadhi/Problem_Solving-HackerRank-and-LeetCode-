def guessNumber(n):
        """
        :type n: int
        :rtype: int
        """
        low=1
        high=n
        if guess(high)==1:
            return high
        s=(low+high)//2
        while True:
            if(e==1):
                low=s
                s=(low+high)//2
                e=guess(s)
            elif(e==-1)    :
                high=s
                s=(low+high)//2
                e=guess(s)
            else:
                return s
