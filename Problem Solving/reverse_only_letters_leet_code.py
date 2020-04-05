a="ab-cd"
a="Test1ng-Leet=code-Q!"
rev_a=""
for item in a[::-1]:
    if item in "AabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        rev_a+=item
a=list(a)
rev_a=list(rev_a)
index_b=0
for i in range(len(a)):
    if (65<=ord(a[i])<=90) or (97<=ord(a[i])<=122):
        a[i]=rev_a[index_b]
        index_b+=1
print(''.join(i for i in a))