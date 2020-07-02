def anagram(s):
    if len(s)%2 !=0:
        return -1
    else:
        half=len(s)//2
        first=Counter(list(s[:half])) #counting no of times each character present in first half of string
        second=Counter(list(s[half:])) #counting no of times each character present in second half of string
        count=0

        for elem in first:
            if elem in second:
                if first[elem]>second[elem]:      #if the element present in second half i need to know whether the character count is same in first if not i need to find out the difference
                    count+=abs(first[elem]-second[elem])
            else:                         #if the charatcer is not present in the second hald but is present in the first then also i need to count the number of times the charatcer present in first but not in second
                count+=first[elem]

        
    return count
