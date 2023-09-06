from simpleQueue import *

globalInstance = Queue()

def isQEmpty():
    assert globalInstance.isQueueEmpty() == 1

def Qelements():
    assert globalInstance.count == 2

def addingToQ():
    assert globalInstance.enque(2) == 1
    assert globalInstance.enque(4) == 2
    assert globalInstance.enque(3) == 3

def deletingQElements():
    assert globalInstance.deque() == 2

def peekingQ():
    assert globalInstance.peekQueue() == 2

def printingQ():
    assert globalInstance.printQElements() == [2,4,3]


isQEmpty()
addingToQ()
printingQ()
peekingQ()
deletingQElements()
Qelements()