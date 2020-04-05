
#a=sorted(a,reverse=True)
for i in range(0,len(a),2):
    if i>0 and a[i-1]<a[i]:
        a[i-1],a[i]=a[i],a[i-1]
    if i<len(a)-1 and a[i]>a[i+1]:
        a[i],a[i+1]=a[i+1],a[i]

print(a[::2])
