def isHappy(a):
    number_generated=[]
    value=a
    while value!=1:
        value=sum([int(i)**2 for i in str(value)])
        if value in number_generated:
            number_generated.append(value)
            return number_generated
        else:
            number_generated.append(value)
    return True
isHappy(1485)