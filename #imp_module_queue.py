#imp using module called queue have class name lifoqueue
import queue
stack1=queue.LifoQueue(3)
# this class have 2 methods for add and remove which is put to add elemnt at the end of stack and get to remove last elemnt from stack
stack1.put(12)
print(stack1)
stack1.put(200)
print(stack1)
# if you exceed the limit of stack this will go for overflow 
# if you pop all elemnts and try to pop empty stack it will go on underflow
# both of them doesnt go on error but on infinte loop