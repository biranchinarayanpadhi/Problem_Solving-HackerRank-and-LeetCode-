def alternatingCharacters(s):
    count=0
    for char in s:
        if char == "A":
            count+=1
    length=len(s)
    if count == length:
        return length-1
    count=0
    for char in s:
        if char == "B":
            count+=1
    if count == length:
        return length-1

    actual_count=0
    for i in range(1,length):
        if s[i] == s[i-1]:
            actual_count+=1
    return actual_count
