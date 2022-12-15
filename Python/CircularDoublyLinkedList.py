class DListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    # def __str__(self):
    #     if self.next is None and self.previous is None:
    #         return f"previous: None self: {id(self)} next: None"

    #     elif self.next is None:
    #         return f"previous: {id(self.previous)} self: {id(self)} next: None"

    #     elif self.previous is None:
    #         return f"previous: None self: {id(self)} next: {id(self.next)}"

    #     return f"previous: {id(self.previous)} self: {id(self)} next: {id(self.next)}"


class CircularDoublyLinkedList:
    """CircularDoublyLinkedList"""

    def __init__(self, values=None):
        """initialise the list with values

        Args:
            values (Iterable): values to be added to list (optional)
        """
        self.head = None
        self.tail = None
        self.length = 0

        if values is None:
            return

        for i in values:
            self.add_at_end(i)

    def add_at_start(self, value):
        """add value at the start of list
        time complexity is O(1)

        Args:
            value (Any): value to be added
        """
        old_head = self.head
        self.head = DListNode(value)

        if old_head is not None:
            old_head.previous = self.head
            self.head.next = old_head
            self.tail.next = self.head
            self.head.previous = self.tail
        else:
            self.head.next = self.head
            self.head.previous = self.head
            self.tail = self.head

        self.length += 1

    def add_at_end(self, value):
        """add value at the end of the list
        time complexity is O(1)

        Args:
            value (Any): value to be added
        """
        if self.length == 0:
            self.head = DListNode(value)
            self.head.next = self.head
            self.head.previous = self.head
            self.tail = self.head
            self.length += 1
            return

        self.tail.next = DListNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        self.tail.next = self.head
        self.head.previous = self.tail
        self.length += 1

    def add_at(self, index, value):
        """add value at the specified index
        time complexity is O(n)

        Args:
            index (int): index to insert at
            value (Any): value to be added

        Raises:
            IndexError: when invalid index or negative index is passed
        """
        if index < 0 or index >= self.length:
            raise IndexError(
                f"Index out of Bound. Length of list {self.length}, index got to insert at {index}."
            )

        if index == 0:
            self.add_at_start(value)
            return

        running_node = self.head
        for _ in range(index - 1):
            running_node = running_node.next

        new_node = DListNode(value)
        new_node.next = running_node.next
        new_node.previous = running_node
        new_node.next.previous = new_node
        running_node.next = new_node
        self.length += 1

    def extend(self, values):
        """add values to the end of the list

        Args:
            values (Iterable): values to be added to list
        """
        for i in values:
            self.add_at_end(i)

    def remove_at_start(self):
        """removes the element at beginning of the list
        time complexity is O(1)

        Raises:
            IndexError: when no element is present in the list

        Returns:
            Any: element at start of the list
        """
        if self.length == 0:
            raise IndexError("No elements in list to remove.")

        node = self.head
        self.head = node.next
        self.tail.next = self.head
        self.head.previous = self.tail

        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

        return node.value

    def remove_at_end(self):
        """remove the element at the end of the list
        time complexity is O(1)

        Raises:
            IndexError: when no element is present

        Returns:
            Any: element at end of the list
        """
        if self.length == 0:
            raise IndexError("No elements in list to remove.")

        node = self.tail
        self.tail = node.previous
        self.tail.next = self.head
        self.head.previous = self.tail

        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

        return node.value

    def remove_at(self, index):
        """remove the element present at the given index
        time complexity is O(n)

        Args:
            index (int): index of the element to be removed

        Raises:
            IndexError: when invalid or negative index is passed

        Returns:
            Any: element at the given index
        """
        if index < 0 or index >= self.length:
            raise IndexError(
                f"Index out of Bound. Length of list {self.length}, index got to insert at {index}."
            )

        if self.length == 1:
            node = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return node.value

        if index == 0:
            return self.remove_at_start()

        if index == self.length - 1:
            return self.remove_at_end()

        running_node = self.head
        for _ in range(index - 1):
            running_node = running_node.next

        node = running_node.next
        running_node.next = node.next
        node.next.previous = running_node
        self.length -= 1

        return node.value

    def remove_by_value(self, value):
        """remove the first occurrence of value in list

        Args:
            value (Any): value of the element to be returned

        Raises:
            ValueError: when no element with the given value is present in the list

        Returns:
            Any: returns the argument value
        """
        i = 0
        running_node = self.head
        while i < self.length:
            if running_node.value == value:
                running_node.previous.next = running_node.next
                running_node.next.previous = running_node.previous
                self.length -= 1

                # update self.head and self.tail if removed from start or end
                if i == 0:
                    self.head = running_node.next
                elif i == self.length:
                    self.tail = running_node.previous

                # set head and tail to None if length is 0
                if self.length == 0:
                    self.head = None
                    self.tail = None

                return running_node.value

            running_node = running_node.next
            i += 1

        raise ValueError("No element with the given value found")

    def __len__(self):
        return self.length

    def __iter__(self):
        return self.iterator()

    def iterator(self):
        """forward iterator

        Yields:
            Any: value of element
        """
        running_node = self.head
        for _ in range(self.length):
            yield running_node.value
            running_node = running_node.next

    def backwards_iterator(self):
        """backwards iterator

        Yields:
            Any: value of element
        """
        running_node = self.tail
        for _ in range(self.length):
            yield running_node.value
            running_node = running_node.previous

    def __getitem__(self, index):
        if index < 0 or index >= self.length:
            raise IndexError(
                f"Index out of Bound. Length of list {self.length}, index to get at is {index}."
            )

        node = self.head
        for _ in range(index):
            node = node.next

        return node.value

    def __setitem__(self, index, value):
        if index < 0 or index >= self.length:
            raise IndexError(
                f"Index out of Bound. Length of list {self.length}, index to get at is {index}."
            )

        node = self.head
        for _ in range(index):
            node = node.next

        node.value = value

    def __str__(self):
        result = "["

        for i in self:
            result += str(i) + ", "

        result += "]"

        return result

    # def __repr__(self):
    #     result = "[\n"

    #     i = self.head
    #     for _ in range(self.length):
    #         result += "\t" + str(i) + ",\n"
    #         i = i.next

    #     result += "]"

    #     return result
