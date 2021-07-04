from .stack import Stack

class Queue:
    def __init__(self):
        self.first = Stack()
        self.second = Stack()

    def add(self, item):
        self.first.push(item)
    
    def remove(self):
        while self.first.peek():
            self.second.push(self.first.pop())

        if not self.second:
            return None

        item = self.second.pop()

        while self.second.peek():
            self.first.push(self.second.pop())

        return item
    
    def peek(self):
        while self.first.peek():
            self.second.push(self.first.pop())
        
        if not self.second:
            return None

        item = self.second.peek()

        while self.second.peek():
            self.first.push(self.second.pop())

        return item
