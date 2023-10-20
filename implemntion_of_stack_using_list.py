# implemntion of stack using list 
# stack only use push and pop methods 
stack=[]
def add_to_stack():
    elemnet=input("enter the elemnt : ")
    stack.append(elemnet)
    print(stack)
def pop_from_stack():
    if len(stack)!=0:
        e=stack.pop()
        print("the removed elemnet is ",e)
    else:
        print("the stack is empty")
while True:
    print("enter number of operation you want to do 1.pop 2.push 3.quite")
    ch=int(input("enter your num "))
    if ch==1:
        pop_from_stack()
    elif ch==2:
        add_to_stack()
    elif ch==3:
        print("thank you for your time ")
        break
    else:
        print("pls enter the right num ")
