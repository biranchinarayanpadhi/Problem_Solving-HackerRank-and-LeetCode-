input()
count = [0]*11
for t in map(int,input().strip().split()):
    count[t] += 1
print(count.index(max(count)))