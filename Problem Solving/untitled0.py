def balanced_brackets_stack(s):
    stack=[]
    if len(s)%2!=0:
        return "NO"
    for i in s:
        if i == '{' or i=='[' or i=='(':
            stack.append(i)
        else:
            if len(stack)==0:
                return "NO"
            last_elem=stack.pop()
            if i==')' and last_elem=="(":
                continue
            elif i=='}' and last_elem=="{":
                continue
            elif i==']' and last_elem=="[":
                continue
            else:
                return "NO"
    if len(stack)==0:
        return "YES"
    else:
        return "NO"
