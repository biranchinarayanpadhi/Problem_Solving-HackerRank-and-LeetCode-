# Complete the palindromeIndex function below.
def palindromeIndex(s):
    i=0
    j=len(s)-1
    while i<j:
        prev=s[i]
        if s[i] != s[j]:
            #print(s[i],s[j])
            if s[i] == s[j-1]:
                if s[i+1] == s[j-2]:
                    #print(s[i],s[j])
                    return j
                else:
                    return i
            else:
                return i

        i+=1
        j-=1 
        if i == j :
            if s[i] != prev:
                return i
    return -1
            

