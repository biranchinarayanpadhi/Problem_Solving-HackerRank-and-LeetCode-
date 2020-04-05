import collections
A=[4,2,5,7]
def sortArrayByParityII(a):
#    dic{}
    count_even=0
    count_odd=0
    even=[]
    odd=[]
    final_list=[]
    for i in a:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    
    for i in range(len(a)):
        if i%2==0:
            final_list.append(even[count_even])
#            dic[even[count_even]]=i
            count_even+=1
        else:
            final_list.append(odd[count_odd])
            count_odd+=1
    
#    dic=collections.OrderedDict(dic)
#    print(list(dic.keys()))
    print(final_list)
    
sortArrayByParityII(A)