class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dicti={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        len1=len(num1)
        len2=len(num2)
        if num1 == '0' or num2 == '0':
            return '0'
        if len1 == 1 and len2 ==1:
            return str(dicti[num1[0]]*dicti[num2[0]])
        if num1 =='1':
            return num2
        if num2 == '1':
            return num1
        
        total_length=len1+len2
        arr=[0]*total_length
        position=total_length-2
        k=total_length-1
        i=len2-1
        j=len1-1
        carry=0
        while i>=0:
            while j>=0:
                product=(dicti[num2[i]]*dicti[num1[j]])+carry
                arr[k]=arr[k]+product
                k-=1
                j-=1
            k=position
            position-=1
            i-=1
            j=len1-1  
            
        print(arr)
        not_zero=0
        carry=0
        res=""
        j=total_length-1
        while j>=0:
            tmp=(arr[j]+carry)%10
            carry=(arr[j]+carry)//10
            arr[j]=tmp
            j-=1
            
        for i in range(total_length):
            if arr[i]!=0:
                not_zero=i
                break
                
        for k in range(not_zero,total_length):
            res+=str(arr[k])
        return res