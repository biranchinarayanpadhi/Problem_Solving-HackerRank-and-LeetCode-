from math import sqrt,atan,degrees
ab=int(input())
bc=int(input())
#ac=round(sqrt(ac),2)
#print(ac)
#mc=round(ac/2,2)
#print(mc)
value=atan(ab/bc)
angle=round(degrees(value))
t = u"\u00b0"
print(str(int(angle))+t)

  
