class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item: object) -> None:
        self.items.insert(0, item)

    def dequeue(self) -> object:
        return self.items.pop()

    def size(self) -> int:
        return len(self.items)
