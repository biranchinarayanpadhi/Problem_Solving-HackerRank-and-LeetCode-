def isPalindrome(s):
    alpha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    s=s.strip()
    string=""
    if len(s)==0:
        return True
    else:
        for i in s:
            if i in alpha:
                string+=i
        string=string.lower()
        print(string)
        print(string[::-1])
        if string==string[::-1]:
            return True
        else:
            return False
    
isPalindrome("0P")
a="ka12"
print(a.isalnum())