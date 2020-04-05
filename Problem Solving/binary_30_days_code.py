n=int(input())
li=[]
binary=str(bin(n))[2:]
counts=0
count=0
print(binary)
for i in range(len(binary)):
    if binary[i]=='1':
        count+=1
    else:
        counts=max(counts,count)
        count=0
print(max(counts,count))