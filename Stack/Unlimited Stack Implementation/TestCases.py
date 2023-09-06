from stackImplementing import *

instance = Stack()

# Chekcking whether the stack is empty are not
def testEmptyStack():
    instance = Stack()
    assert instance.isStackEmpty() == True
# testEmptyStack()

# Pushing the element into the stack
def push():
    instance.stackPush(10)
    instance.stackPush(20)
    instance.stackPush(30)

    assert instance.stackLength() == 3
push()

# Popping the elements of the stack
def pop():
    assert instance.stackPop() == 30
pop()

# Printing the elments of the list
def printElements():
    assert instance.printStackElements() == [10,20]
printElements()

# Peeking into the stack
def peekStack():
    assert instance.stackPeek() == (20)
peekStack()

print(instance)