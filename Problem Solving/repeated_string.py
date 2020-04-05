def repeatedString(a, n):
    if len(a)==1 and a=="a":
        return n
    counted=a.count("a")
    quotient=n//len(a)
    remainder=n%len(a)
    counted=counted*quotient
    repeated_string=a[:remainder]

    return (counted+repeated_string.count('a'))

