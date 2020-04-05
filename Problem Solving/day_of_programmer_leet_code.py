def day_of_programmer(year):
    if 1700<=year<=1917:
        if year%4==0:
            return "12.09."+str(year)
        else:
            return "13.09."+str(year)
    elif year==1918:
        return "26.09."+year
    else:
        if((year%4==0 and year%100!=0 )or (year%400==0)):
            return "12.09."+str(year)
        else:
            return "13.09."+str(year)

year=1918
print(day_of_programmer(year))







