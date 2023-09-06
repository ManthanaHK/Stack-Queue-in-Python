class Stack:
    def __init__(self):
        self.data = []
        self.count = 0
        self.size = 4
    
    def isStackEmpty(self):
        return self.count == 0
    
    def stackSize(self):
        return self.size
    
    def pushStack(self,ele):      
        if self.count < self.size:
            self.data.append(ele)
            self.count += 1
        else:
            return 0
    
    def popStack(self):
        if not self.isStackEmpty():
            self.count -= 1
            return self.data.pop()
        else:
            return 0
    
    def printElements(self):
        if not self.isStackEmpty():
            return self.data
        else:
            return 0
    
    def peekStack(self):
        if not self.isStackEmpty():
            return self.data[-1]
        else:
            return 0