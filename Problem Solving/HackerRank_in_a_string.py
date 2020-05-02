def hackerrankInString(s):
    my_string="hackerrank"
    s=s.lower()
    char_starting_dicti={}
    new_dicti={}
    res=[]
    length=len(s)
    for i in range(length):
        if s[i] == " ":
            continue
        elif s[i] not in char_starting_dicti:
            char_starting_dicti[s[i]]=[i]
        else:
            char_starting_dicti[s[i]].append(i)
    
    if "h" in char_starting_dicti:
        new_dicti["h"]=char_starting_dicti["h"][0]
        res.append(char_starting_dicti["h"][0])
    else:
        return "NO"
    for i in range(1,len(my_string)):
        elem=my_string[i]
        if elem in char_starting_dicti:
            value=new_dicti[my_string[i-1]]
            flag=0
            arr=char_starting_dicti[elem]
            for val in char_starting_dicti[elem]:
                if val>value:
                    res.append(val)
                    new_dicti[elem]=val
                    flag=1
                    break
            if flag == 0:
                return "NO"
        else:
            return "NO"
    print(res)
    return "YES"
            
