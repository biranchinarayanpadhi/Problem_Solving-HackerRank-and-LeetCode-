def combine(s):
    even_s=""
    odd_s=""
    for i in range(len(s)):
        if i%2==0:
            even_s=even_s+s[i]
        else:
            odd_s=odd_s+s[i]
    print(even_s,odd_s)

if __name__=="__main__":
    n=int(input())
    for i in range(n):
        s=input()
        combine(s)
        
a=[1,2,3,4]
a=list(reversed(a))
for i in a:
    print(a,"\t")
