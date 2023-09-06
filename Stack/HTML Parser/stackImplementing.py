class Stack:
    def __init__(self):
        self.data = []
        self.count = 0
    
    def isStackEmpty(self):
        return self.count == 0
    
    def stackLength(self):
        return self.count
    
    def stackPush(self,ele):
        self.data.append(ele)
        self.count += 1
    
    def stackPop(self):
        if not self.isStackEmpty():
            self.count -= 1
            return self.data.pop()
        else:
            return 0
    
    def printStackElements(self):
        if not self.isStackEmpty():
            return self.data
        else:
            0
    
    def stackPeek(self):
        if not self.isStackEmpty():
            return self.data[-1]
        else:
            0