def angryProfessor(k, a):
    a.sort()
    before_begin=0
    for i in a:
        if i<=0:
            before_begin+=1
    if before_begin>=k:
        return "NO"
    else:
        return "YES"

angryProfessor(4,[-93,86,49,-62,-90,-63,40,72,11,67])