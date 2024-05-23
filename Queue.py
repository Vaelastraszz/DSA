class Queue:
    def __init__(self):
        """Creates a new queue that is empty."""
        self.items = []

    def isEmpty(self):
        """Tests to see whether the queue is empty."""
        return self.items == []

    def enqueue(self, item: object) -> None:
        """Adds a new item to the rear of the queue.

        Args : item : object : the item to be added to the queue."""
        self.items.append(item)

    def dequeue(self) -> object:
        """Removes and returns the front item from the queue.

        Returns : object : the front item of the queue."""
        return self.items.pop(0)

    def size(self) -> int:
        """Returns the number of items in the queue.
        It needs no parameters and returns an integer.

        Returns : int : the number of items in the queue."""
        return len(self.items)
