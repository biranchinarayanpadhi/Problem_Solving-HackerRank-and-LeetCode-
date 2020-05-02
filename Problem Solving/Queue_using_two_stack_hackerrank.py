# Enter your code here. Read input from STDIN. Print output to STDOUT
stack1=[]
stack2=[]

def dequeu():
    if len(stack2) >0:
        return stack2.pop()
    else:
        while len(stack1) != 0:
            stack2.append(stack1.pop())
        return stack2.pop()

if __name__ == "__main__":

    no_of_parameter=int(input())

    for i in range(no_of_parameter):
        input_parameters=list((input().rstrip().split()))

        if input_parameters[0] == "1":
            stack1.append(int(input_parameters[1]))
        elif input_parameters[0] == "2":
            dequeu()
        else:
            value=dequeu()
            stack2.append(value)
            print(value)


