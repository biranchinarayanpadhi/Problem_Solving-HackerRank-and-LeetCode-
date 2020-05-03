def appendAndDelete(s, t, k):

    len_s=len(s)
    len_t=len(t)
    index=0
    count=0
    if s[index]!=t[index]:
        count=len_s+len_t
        if k>=count:
            return "Yes"
        else:
            return "No"
    
    else:
        while index<len_s and index<len_t:
                if s[index] != t[index]:
                    break
                index+=1
        
        if index>=len_s and index >= len_t:
            return "Yes"

        elif index>=len_s: #for ex: s=aaa t=aaabbb k=6
            count=len_t-index
            if count ==1 and k%2==0:
                return "No" 
            elif k%count!=0:
                return "No"
            else:
                return "Yes"

        elif index>=len_t: #for ex: s=aaabbb t=aaabb k=6
            count=(len_s-index)
            print(count)
            if count ==1 and k%2==0:
                return "No"
            elif k<=count :
                return "No"
            else:
                return "Yes"
        else:
            count=(len_s-index)+(len_t-index)
            if count <= k:
                return "Yes"
            else:
                return "No"
