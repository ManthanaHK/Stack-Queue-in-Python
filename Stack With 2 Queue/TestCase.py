from stack2Q import *

globalInstnace1 = Queue1()
globalInstance2 = Queue2()

def push(ele):
    globalInstnace1.enque(ele)
    print("Data" + str(globalInstnace1.data))
    
push(3)