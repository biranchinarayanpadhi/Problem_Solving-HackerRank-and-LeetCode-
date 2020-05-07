def beautifulBinaryString(b):
    given_string=b
    length=len(b)
    if length<3:
        return 0
    count=index=0
    sub_str="010"
    while index < length-2:
        if given_string[index:index+3] == sub_str:
            count+=1
            index+=3
        else:
            index+=1
    return count
