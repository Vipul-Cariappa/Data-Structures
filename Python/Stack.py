from DoublyLinkedList import DoublyLinkedList
import math


class Stack(DoublyLinkedList):
    """Stack
    Implemented using a Doubly Linked List"""

    def __init__(self):
        """initializer"""
        super().__init__()

    def push(self, value):
        """push an element to the top of the stack

        Args:
            value (Any): element to be pushed
        """
        self.add_at_end(value)

    def pop(self):
        """pop the top most element and return the value

        Returns:
            Any: value of top most element
        """
        return self.remove_at_end()

    def peek(self):
        """get the value of top most element without removing it

        Raises:
            IndexError: when no element is present

        Returns:
            Any: value of the top most element
        """
        if self.length:
            return self.tail.value

        raise IndexError("No elements in list.")

    def __str__(self):
        if self.length == 0:
            return "+---+"

        result_string = ""
        element_str = [(j := str(i), len(j)) for i in self.backwards_iterator()]
        max_str_len = max(i[1] for i in element_str) + 2
        end_strings = "+" + "-" * max_str_len + "+" + "\n"
        result_string += end_strings

        for string, length in element_str:
            start_space = math.floor((max_str_len - length) / 2)
            end_space = math.ceil((max_str_len - length) / 2)
            result_string += (
                "|"
                + " " * start_space
                + string
                + " " * end_space
                + "|"
                + "\n"
                + end_strings
            )

        return result_string
