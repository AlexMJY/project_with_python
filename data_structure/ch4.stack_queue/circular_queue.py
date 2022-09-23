class CQueue:
    MAXSIZE = 10
    def __init__(self):
        self.container = [None for _ in range(CQueue.MAXSIZE)]
        self.front = 0
        self.rear = 0
        
    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False
    
    def is_full(self):
        next = self.__step_forward(self.rear)
        if next == self.front:
            return True
        else:
            return False