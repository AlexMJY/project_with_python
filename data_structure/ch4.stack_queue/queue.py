class Queue:
    def __init__(self):
        self.container = list()
        
        def empty(self):
            if not self.container:
                return True
            else:
                return False
            
        def enqueue(self, data):
            return self.container.append(data)
        
        def dequeue(self):
            return self.container.pop(0)
        
        def peek(self):
            return self.container[0]