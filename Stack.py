class Stack:
    def __init__(self):
        """Creates a new stack that is empty.

        Args : None

        Returns : None"""
        self.stack = []

    def push(self, element):
        """Adds a new element to the top of the stack.

        Args : element : object : the element to be added to the stack.

        Returns : None"""
        self.stack.append(element)

    def pop(self):
        """Removes and returns the top element from the stack.

        Args : None

        Returns : object : the top element of the stack.
        If the stack is empty, returns None."""
        if self.is_empty():
            return None
        return self.stack.pop()

    def is_empty(self):
        """Tests to see whether the stack is empty.

        Args : None

        Returns : bool : True if the stack is empty, False otherwise."""
        return len(self.stack) == 0

    def peek(self):
        """Returns the top element of the stack.

        Args : None

        Returns : object : the top element of the stack."""
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        """Returns the number of elements in the stack.

        Args : None

        Returns : int : the number of elements in the stack."""

        return len(self.stack)


if __name__ == "__main__":
    # Test the Stack class
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.is_empty())
    print(stack.size())
    print(stack.peek())
    stack.push(4)
    print(stack.peek())
    print(stack.size())
