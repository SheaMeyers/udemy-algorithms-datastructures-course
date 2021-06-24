class Queue:
    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.append(item)
    
    def remove(self):
        if not self.queue:
            return None

        return self.queue.pop(0)
    
    def peek(self):
        if not self.queue:
            return None

        return self.queue[0]
    
def weave(sourceOne, sourceTwo):
    queue = Queue()

    while (sourceOne.peek() or sourceTwo.peek()):
        if sourceOne.peek():
            queue.add(sourceOne.remove())
        if sourceTwo.peek():
            queue.add(sourceTwo.remove())
    
    return queue
