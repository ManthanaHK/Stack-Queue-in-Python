from simpleQueue import *

instance = Queue()

def rotating():
    instance.enque(10)
    instance.enque(20)
    instance.enque(30)

    old = instance.data[:3]

    for i in range(1,len(old)+1):
        instance.enque(old[-i])
    return instance.data

assert rotating() == ([10,20,30,30,20,10])