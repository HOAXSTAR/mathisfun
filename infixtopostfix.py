#defining stack to store operators
stack = []
top= -1
def push(a):
    global top
    top +=1
    stack.append(a)
    #print(a, " is pushed at top")
def pop():
    global top
    if top == -1:
        #print("Underflow")
        return
   # print("poped element ",stack[top])
    stack.pop()
    top -= 1 
def show():
    c = top 
    if top == -1:
        print("Stck is empty :(")
        return
    while(c>=0):
        print(stack[c])
        c -= 1
# function to get postfix notation
def post(inpt):
    post= []
    closebrc = ")}]"
    openbrc = "({["
    op = "/*+-"
    for i in range(len(inpt)):
        if (ord(inpt[i])>=97 and ord(inpt[i])<=122) or(ord(inpt[i])>=65 and ord(inpt[i])<=90):
            post.append(inpt[i])
        else:
            if len(stack)>=1 and stack[top] in op and inpt[i] in op:
                ind = op.index(inpt[i])
                if ind == 0:
                    push(inpt[i])
                elif ind == 1 and stack[top] != "/":
                    push(inpt[i])
                # elif ind == 3 and stack[top]=="+":
                #     push(inpt[i])
                else:
                    post.append(stack[top])
                    pop()
                    push(inpt[i])      
            else:
                push(inpt[i])
        if inpt[i] in closebrc:
            ind = closebrc.index(inpt[i])
            pop()
            while(ord(stack[top]) != ord(openbrc[ind])):
                post.append(stack[top])
                pop()
            pop()
    while(top!=-1):
        post.append(stack[top])
        pop()
    result = "".join([i for i in post]) 
    return result
#function to get reversed input
def reverse(inpt):
    braces_C = ")}]"
    braces_O = "({["
    rev =""
    for i in reversed(inpt):
        if i in braces_C:
            ind = braces_C.index(i)
            rev += rev.join(braces_O[ind])
        elif i in braces_O:
            ind = braces_O.index(i)
            rev += rev.join(braces_C[ind])
        else:
            rev += rev.join(i)
    return rev
print("Please select your option: \n1: InFix to PostFix\n2: InFix to PreFix\nAny number to Exit!!!")
choice= int(input("Enter your choice: "))
while choice== 1 or choice == 2:
    if choice == 1:
        inpt = input("Enter the InFix Input: ")
        postfix = post(inpt)
        print("PostFix notation: ",postfix)   
        choice= int(input("\nEnter your choice: "))
    else:
        inpt = input("Enter the InFix Input: ")
        inpt = reverse(inpt)
        rev_post= post(inpt)
        pre = "".join([i for i in reversed(rev_post)])
        print("PreFix notation : ",pre)
        choice= int(input("\nEnter your choice: "))
print("Exit!!!")   
    
