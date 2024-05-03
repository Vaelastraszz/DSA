class Node:
    """
    Represents a node in a linked list.

    Attributes:
        data: The data stored in the node.
        next: A reference to the next node in the linked list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None
        Linked_Node.count_nodes += 1


class Linked_Node:
    """
    Represents a linked list node.

    Attributes:
        head: The head node of the linked list.
    """

    count_nodes = 0

    def __init__(self):
        self.head = None

    def append(self, data: int):
        """
        Appends a new node with the given data to the linked list.

        Args:
            data (int): The data to be added to the new node.

        Returns:
            str: A message indicating the result of the operation.
        """
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return f"Node with data {data} is added as head."
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
            return f"Node with data {data} is added."

    def delete(self, data: int):
        """
        Deletes the node with the given data from the linked list.

        Args:
            data (int): The data of the node to be deleted.

        Returns:
            str: A message indicating the result of the operation.
        """
        if self.head == None:
            return f"Linked list is empty."
        elif self.head.data == data and self.head.next == None:
            self.head = None
            return f"Linked list is now empty head is deleted."
        elif self.head.data == data:
            self.head = self.head.next
            return f"Node with data {data} is deleted. Head is updated."

        temp = self.head
        while temp.next:
            if temp.next.data == data:
                if temp.next.next:
                    temp.next = temp.next.next
                    return f"Node with data {data} is deleted."
                else:
                    temp.next = None
                    return f"Node with data {data} is deleted. Last node is deleted."
            temp = temp.next
        return f"Node with data {data} is not found."

    @classmethod
    def get_count_nodes(cls):
        """
        Returns the number of nodes in the linked list.

        Returns:
            str: A message indicating the number of nodes in the linked list.
        """
        return f"Number of Nodes in the Linked_list: {cls.count_nodes}"


if __name__ == "__main__":
    linked_list = Linked_Node()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    print(linked_list.get_count_nodes())
