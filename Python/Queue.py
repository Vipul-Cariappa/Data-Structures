from DoublyLinkedList import DoublyLinkedList


class Queue(DoublyLinkedList):
    """Queue
    Implemented using a Doubly Linked List"""

    def __init__(self):
        """initializer"""
        super().__init__()

    def enqueue(self, value):
        """insert an element at the end of the queue

        Args:
            value (Any): element to be inserted
        """
        self.add_at_end(value)

    def dequeue(self):
        """remove and return the value of the first element in the queue

        Returns:
            Any: value of the first element
        """
        return self.remove_at_start()

    def peek(self):
        """gets the value of first element in the queue without removing it

        Raises:
            IndexError: when no element is present

        Returns:
            Any: value of the first element
        """
        if self.length:
            return self.head.value

        raise IndexError("No elements in list.")
