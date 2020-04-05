def timeConversion(s):
    time_info=s[len(s)-2:len(s)]
    if(time_info=='AM'):
        if((s[0:2])=="12"):
            strs="00"+s[2:len(s)-2]
            return strs
        else:
            return s[0:len(s)-2]
    else:
        if(int(s[0:2]))==12:
            return s[0:len(s)-2]
        else:
            strs=int(s[0:2])+12
            strs=str(strs)+s[2:len(s)-2]
            return strs
timeConversion("12:45:23AM")
