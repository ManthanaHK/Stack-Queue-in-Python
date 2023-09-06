#Implementing stack using 2 queues

from simpleQueue import *

class stackUsingQueue:
    def __init__(self):
        self.q1=Queue()
        self.q2=Queue()
    #enquing the element to queue is same as pushin the element to stack
    def pushNew(self,ele):
        self.q1.enque(ele)
        return self.q1.count
    #Popping the element from stack should give top element but dequeue operation will give the rear element.
    #So dequeue element from Q1 and enqueue to Q2 until the last elemnt found. The last element is popped. Again all elements from Q2 will be enqued back to Q1
    def popNew(self):
        while(self.q1.getElementCount()>1):
            self.q2.enque(self.q1.deque())
        ele=self.q1.deque()
        while(self.q2.getElementCount()>0):
            self.q1.enque(self.q2.deque())
        return ele
    def peekNew(self):
        while(self.q1.getElementCount()>1):
            self.q2.enque(self.q1.dequeue())
        ele=self.q1.peekQueue()
        self.q2.enque(self.q1.deque())
        while(self.q2.getElementCount()>0):
            self.q1.enque(self.q2.deque())
        return ele
    

s1=stackUsingQueue()
assert(s1.pushNew(10)==1)
assert(s1.pushNew(20)==2)
assert(s1.pushNew(30)==3)
assert(s1.popNew()==30)
assert(s1.peekNew()==20)