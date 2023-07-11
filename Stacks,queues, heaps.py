##-------------STACKS--------------
# IT USES
# LIFO (LAST IN FIRST OUT ) DATA STRUCTURE
# USE APPEND TO PUSH AN ITEM ON THE STACK
# THEN POP TO REMOVE AN ITEM FROM IT
my_stack=list()
my_stack.append(2)
my_stack.append(6)
my_stack.append(65)
my_stack.append(43)
print(my_stack)
print(my_stack.pop(2))
print(my_stack.pop())
print(my_stack)
class Stack():
    def __init__(self):
        self.stack= list()
    def push(self,item):
        self.stack.append(item)
    def pop(self):

        if len(self.stack)>0:
            return self.stack.pop()
        else :
            return None
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None
    def __str__(self):
        return str(self.stack)
my_stack=Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack)
print(my_stack.pop())
print(my_stack.peek())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())


#-------------------QUEUES--------------------
# USES -------FIRST IN FIRST OUT------- DATA STRUCTURE
# ENQUEUE --------ADD -----------AN ITEM TO THE ------END----- OF THE LINE
# DEQUEUE --------REMOVE-------- AN ITEM FROM THE ----FRONT---- OF THE LINE
# SO YOU ENQUEUE ON ONE END AND DEQUEUE ON THE OTHER END
#
from collections import deque
my_queue=deque()
my_queue.append(5)
my_queue.append(10)
print(my_queue)
print(my_queue.popleft())                       # THIS POPS THE FIRST ITEM AS WE DISCUSSED
class Queue():
    def __init__(self):
        self.queue=[]
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue)>0:
            return self.queue.pop(0)
        else :
            return None
    def __str__(self):
        return str(self.queue)
thequeue=Queue()
thequeue.enqueue(2)
thequeue.enqueue(5)
thequeue.enqueue(10)
print(thequeue)
print(thequeue.dequeue())
#
#
#------------------HEAPS-------------------