def superReducedString(s):
    b=list(s)
    i=0
    while i+1<len(b):
        if b[i]==b[i+1]:
#            print(i,i+1)
            b.pop(i)
            b.pop(i)
            return superReducedString(''.join(b))
        else: 
            i+=1
    if b==[]:
        return("Empty String")
    else:
        return(''.join(b))

a="aaabccddd"
superReducedString(a)