from dynamicQueue import *

globalInstance = DynamicQueue()

def add():
    assert globalInstance.enque(2) == 1 
    assert globalInstance.enque(16) == 2
    assert globalInstance.enque(18) == 3
    assert globalInstance.enque(90) == 4
    assert globalInstance.deque() == 2
    assert globalInstance.enque(22) == 4
    assert globalInstance.enque(164) == 5
    assert globalInstance.enque(138) == 6


add()
print(globalInstance.printQ())