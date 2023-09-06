class Queue:
    def __init__(self):
        self.data = []
        self.count = 0
    
    def isQueueEmpty(self):
        return self.count == 0
    
    def getElementCount(self):
        return self.count
    
    def enque(self,ele):
        self.data.append(ele)
        self.count = self.count + 1
        return self.count
    
    def deque(self):
        if not self.isQueueEmpty():
            self.count = self.count - 1
            return self.data.pop(0)
        else:
            return False
    
    def peekQueue(self):
        return self.data[0]
    
    def printQElements(self):
        if not self.isQueueEmpty():
            return self.data
        else:
            return False