def funnyString(s):
    t=s[::-1]
    for i in range(len(s)-1):
        if abs(ord(s[i])-ord(s[i+1]))==abs(ord(t[i])-ord(t[i+1])):
           continue
        else:
            return ("Not Funny")
    return "Funny"
