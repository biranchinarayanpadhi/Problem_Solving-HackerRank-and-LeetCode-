kal=["give","me","one","grand","today"]
br=["give","one","grand","today"]
def checkMagazine(magazine, note):
    dictis={}
    for i in magazine:
        if i in dictis:
            dictis[i]+=1
        else:
            dictis[i]=0
    for j in note:
        if j not in dictis:
            return "No"
        elif j in dictis and dictis[j]>=0:
            dictis[j]-=1
            continue
        else:
            return "No"
    return "Yes"
checkMagazine(kal,br)    