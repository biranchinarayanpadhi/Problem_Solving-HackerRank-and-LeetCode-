def cookies(a,k,count):
  flag=0
  for i in a:
      if i<k:
          flag=1
  if flag==1:    
      while True:  
              if len(a)==1 and a[0]<k:
                  return -1
              min_a=min(a)
              a.remove(min_a)
              print(a)
              min_b=min(a)
              a.remove(min_b)
              result=1*min_a+2*min_b
              a.append(result)
              count+=1
              return cookies(a,k,count)
  return count
#sums=0
a=[1,2,3,9,10,12]
cookies(a,7,0)