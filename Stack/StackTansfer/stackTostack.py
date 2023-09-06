from stackImplementing import *

instance1 = Stack()
instance2 = Stack()

def Transfer():
    instance1.stackPush(10)
    instance1.stackPush(20)
    instance1.stackPush(30)

    tempList = []
    for i in instance1.data:
        tempList.append(i)
    for i in tempList:
        instance2.stackPush(i)
    
    return instance1.data, instance2.data


assert Transfer() == ([10,20,30],[10,20,30])