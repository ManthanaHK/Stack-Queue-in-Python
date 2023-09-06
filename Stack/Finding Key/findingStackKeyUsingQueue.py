#Program to check if key is present in the given stack using one stack and queue

from stackImplementing import *
from simpleQueue import*

s1= Stack()
q1= Queue()

def findKey(key):
    s1.stackPush(10)
    s1.stackPush(20)
    s1.stackPush(30)
    s1.stackPush(40)
    f=0
    
    while(s1.count>0):
        ele=s1.stackPop()
        q1.enque(ele)
        if(key==ele):
            f=1
    copyQueueToStack()
    copyStackToQueue()
    copyQueueToStack()
    return f==1

def copyQueueToStack():
    while(q1.getElementCount() < 0):
        s1.stackPush(q1.deque())

def copyStackToQueue():
    while(s1.stackLength()>0):
        q1.enque(s1.stackPop())

assert(findKey(20)==True)
assert(findKey(200)==False)