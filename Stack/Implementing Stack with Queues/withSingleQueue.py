#Program to implement stack using single queue

from simpleQueue import *

class stackSingleQueue:
    def __init__(self):
        self.q1=Queue()
    def push(self,ele):
        self.q1.enque(ele)
        return self.q1.count
    #Unitl the length of the queue every element is dequeued and enqueued back to the same queue and last element is dequeued and returned
    def pop(self):
        c=self.q1.count
        while(c>1):
            self.q1.enque(self.q1.deque())
            c-=1
        ele=self.q1.deque()
        while(c>1):
            self.q1.enque(self.q1.deque())
            c-=1
        return ele
    def peek(self):
        c=self.q1.count
        while(c>1):
            self.q1.enque(self.q1.deque())
            c-=1
        ele=self.q1.peekQueue()
        self.q1.enque(self.q1.deque())
        while(c>1):
            self.q1.enque(self.q1.deque())
            c-=1
        return ele
    

s1=stackSingleQueue()
s1.push(10)
assert(s1.peek()==10)
s1.push(20)
s1.push(30)
s1.push(50)
assert(s1.peek()==50)
assert(s1.pop()==50)
assert(s1.pop()==30)
assert(s1.peek()==20)