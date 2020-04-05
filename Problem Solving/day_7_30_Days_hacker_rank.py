n=int(input())
dictis={}
for i in range(n):
    name=input()
    lists=name.split(" ")
    # print(lists)
    name=lists[0]
    number=int(lists[1])
    dictis[name]=number
    
for i in range(n):
    names=input()
    if names in dictis:
        print("{}={}".format(names,dictis[names]))
    else:
        print("Not found")
