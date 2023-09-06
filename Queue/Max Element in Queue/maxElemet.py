from simpleQueue import *

instance = Queue()

def findMax():
    instance.enque(-10)
    instance.enque(-20)
    instance.enque(-30)

    max = instance.data[0]
    for i in instance.data:
        if i > max:
            max = i
    return max

assert findMax() == -10