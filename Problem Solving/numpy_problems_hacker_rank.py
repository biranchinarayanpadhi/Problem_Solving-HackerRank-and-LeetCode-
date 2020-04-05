#problem 2
import numpy as np
n, m = map(int, input().split())
array = np.array([input().strip().split() for _ in range(n)], int)
print (array.transpose())
print (array.flatten())

#problem 3
import numpy as np
m, n, p = map(int,input().split())
arr_A = np.array([input().split() for _ in range(m)],int)
arr_B = np.array([input().split() for _ in range(n)],int)
print(np.concatenate((arr_A, arr_B), axis = 0))


#problem 3
nums=tuple(map(int,input().split()))
zero=np.zeros(nums,dtype=np.int)
one=np.ones(nums,dtype=np.int)
print(zero)
print(one)

#problem 4
import numpy as np
n,m=map(int,input().split())
arrs=np.eye(n,m)
arrs=str(arrs).replace('1',' 1').replace('0',' 0')
print(arrs)

#problem 6
import numpy as np
n,m=map(int,input().split())
a_array=np.array([input().split()for i in range(n)],int)
b_array=np.array([input().split() for i in range(n)],int)

print(a_array+b_array)
print(a_array-b_array)
print(a_array*b_array)
print(a_array//b_array)
print(a_array%b_array)
print(a_array**b_array)

#problem 7
import numpy as np
arr=np.array([input().split() for i in range(9)],float)
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))

#problem 8
import numpy as np
n,m=map(int,input().split())
array=np.array([input().split() for i in range(n)],int)
min=np.min(array,axis=1)
max=np.max(min)
print(max)

















