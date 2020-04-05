def circularArrayRotation(a, k, queries):
    determined_k=k%len(a)
    result=rotatedArray(a,determined_k)
    li=[]
    for i in queries:
        li.append(result[i])
    return li

def rotatedArray(a,k):
    li=[]
    for i in range(len(a)-k,len(a)):
        li.append(a[i])
    for i in range(0,len(a)-k):
        li.append(a[i])
    return li

a=[1,2,3]
circularArrayRotation(a,2,[0,1,2])