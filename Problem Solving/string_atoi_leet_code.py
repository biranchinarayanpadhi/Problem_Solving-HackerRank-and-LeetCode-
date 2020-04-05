class Solution:
    def myAtoi(self,st):
        if len(st)==0:
            return 0
        st=st.strip()
        if len(st)==0:
            return 0
        total=0
        value=1
        init_value=0
        first_char=st[0]
        if first_char=='+':
            value=1
            init_value+=1
        elif first_char=='-':
            value=-1
            init_value+=1
        for i in st[init_value:len(st)]:
            if i not in "0123456789":
                return total*value
            total=total*10+int(i)
            if value==1 and total*value>=(2**31):
                return (2**31-1)
            if value==-1 and total*value<=(-2**31):
                return (-2**31)

        return total*value        