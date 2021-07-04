class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)
    
    def pop(self):
        if not self.data:
            return None

        return self.data.pop()
    
    def peek(self):
        if not self.data:
            return None

        return self.data[len(self.data) - 1]
