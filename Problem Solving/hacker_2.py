def wrap(string,max_width):
    s=""
    for i in range(0,len(string),max_width):
        s=s+(string[i:i+max_width])+'\n'
    return (s)

    

result=wrap('ABCDEFGHIJKLMNOPQRSTUVWXYZ',4)
print(result)