n=5
binary=str(bin(n))[2:]
print(binary)
count=0
max_ones=0
for i in binary:
    if i=='1':
        count+=1
    else:
        count=0
    max_ones=max(count,max_ones)

print(max_ones)