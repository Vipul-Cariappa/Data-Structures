class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        if self.next is None:
            return f"self: {id(self)} next: None"

        return f"self: {id(self)} next: {id(self.next)}"


class LinkedList:
    """LinkedList"""

    def __init__(self, values=None):
        """initialise the list with values

        Args:
            values (Iterable): value to be added to LinkedList
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
        self.head = ListNode(value)
        self.head.next = old_head

        if self.length == 0:
            self.tail = self.head

        self.length += 1

    def add_at_end(self, value):
        """add value at the end of the list
        time complexity is O(1)

        Args:
            value (Any): value to be added
        """
        if self.length == 0:
            self.head = ListNode(value)
            self.tail = self.head
            self.length += 1
            return

        self.tail.next = ListNode(value)
        self.tail = self.tail.next
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

        new_node = ListNode(value)
        new_node.next = running_node.next
        running_node.next = new_node
        self.length += 1

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

        self.length -= 1
        if self.length == 0:
            self.tail = None

        return node.value

    def remove_at_end(self):
        """remove the element at the end of the list
        time complexity is O(n)

        Raises:
            IndexError: when no element is present

        Returns:
            Any: element at end of the list
        """
        if self.length == 0:
            raise IndexError("No elements in list to remove.")

        if self.length == 1:
            node = self.head
            self.head = None
            self.length -= 1
            return node.value

        running_node = self.head
        for _ in range(self.length - 2):
            running_node = running_node.next

        node = running_node.next
        running_node.next = None
        self.length -= 1
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

        if index == 0:
            return self.remove_at_start()

        running_node = self.head
        for _ in range(index - 1):
            running_node = running_node.next

        node = running_node.next
        running_node.next = node.next
        self.length -= 1

        return node.value

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

    def __getitem__(self, index):
        if index < 0 or index >= self.length:
            raise IndexError(
                f"Index out of Bound. Length of list {self.length}, index to get at is {index}."
            )

        node = self.head
        for i in range(index):
            node = node.next

        return node.value

    def __setitem__(self, index, value):
        if index < 0 or index >= self.length:
            raise IndexError(
                f"Index out of Bound. Length of list {self.length}, index to get at is {index}."
            )

        node = self.head
        for i in range(index):
            node = node.next

        node.value = value

    def __str__(self):
        result = "["

        for i in self:
            result += str(i) + ", "

        result += "]"

        return result

    def __repr__(self):
        result = "[\n"

        i = self.head
        while i is not None:
            result += "\t" + str(i) + ",\n"
            i = i.next

        result += "]"

        return result
