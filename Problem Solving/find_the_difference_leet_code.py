from collections import Counter
s="kalia"
t="kaliaa"
Counter(t)-Counter(s)
print(list(Counter(t)-Counter(s))[0])
        