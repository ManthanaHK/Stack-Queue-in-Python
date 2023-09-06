from stackImplementation import *

instance = Stack()

# Checking whether the stack is empty
def emptyStack():
    assert instance.isStackEmpty() == True
emptyStack()

# Checking the size of the stack
def stackSize():
    assert instance.size == 4
stackSize()

# Pushing the elements into the stack
def push():
    instance.pushStack(10)
    instance.pushStack(20)
    instance.pushStack(30)
    instance.pushStack(30)
    instance.pushStack(30)
    instance.pushStack(30)
    assert instance.count == 4
push()

# Popping the element of the element
def pop():
    instance.popStack()
    assert instance.count == 3
pop()

def printStack():
    print(instance.printElements())
printStack()