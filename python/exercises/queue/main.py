class Queue:
    queue = []

    def add(self, item):
        self.queue.append(item)
    
    def remove(self):
        if not self.queue:
            return None

        return self.queue.pop(0)
        