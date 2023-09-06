class DynamicQueue:
    
    def __init__(self):
        self.data = []
        self.count = 0
        self.size = 3

    def isQueueEmpty(self):
        return self.count == 0
    
    def getElementsCount(self):
        return self.count
    
    def enque(self,ele):
        if self.count == self.size:
            print("Queue is filled, with {} elements".format(len(self.data)))
            extra = int(input("How many more elements to be added: "))
            self.resizeQueue(extra)
            self.data.append(ele)
            self.count += 1
            return self.count

        else:
            self.data.append(ele)
            self.count = self.count + 1
            return self.count
    
    def deque(self):
        if not self.isQueueEmpty():
            self.count = self.count - 1
            self.size = self.size - 1
            return self.data.pop(0)
        else:
            return False
    
    def resizeQueue(self,extra):
        self.size = extra + self.size

    def printQ(self):
        return self.data