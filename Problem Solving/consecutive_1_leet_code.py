nums=[1,1,1,0,0,1,1]
count=0
max_ones=0
for i in nums:
    if i==1:
        count+=1
    else:
        count=0
    max_ones=max(count,max_ones)

print(max_ones)

#another logic

#if len(nums)==0:
#    print(0)
#
#prev_count,count=0,0
#for i in nums:
#    if i==1:
#        count+=1
#    else:
#        if count>prev_count:
#            prev_count=count
#        count=0
#
#if prev_count==0 or count>prev_count:
#    print(count)
#else:
#    print(prev_count)