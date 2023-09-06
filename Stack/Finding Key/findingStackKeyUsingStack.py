#Program to check if key is present in the given stack using 2 stacks


from stackImplementing import *
from simpleQueue import *
s1 = Stack()
s2 = Stack()
def findKey(key):
    s1.stackPush(10)
    s1.stackPush(20)
    s1.stackPush(30)
    f=0
    while(s1.stackLength()>0):
        ele=s1.stackPop()
        s2.stackPush(ele)
        if(key==ele):
            f=1
    while(s2.count>0):
        s1.stackPush(s2.stackPop())
    return f==1
assert(findKey(20)==True)
assert(findKey(100)==False)