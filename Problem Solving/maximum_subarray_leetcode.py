#a=[-2,-5,6,-2,-3,1,5,-6]
b=[-2,1,-3,4,-1,2,1,-5,4]
c=[-2]
current_max=c[0]
global_max=c[0]

for i in range(len(c)):
   current_max=max(c[i],current_max+c[i])
   if current_max>global_max:
       global_max=current_max
print(current_max,global_max)
