class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        if self.next == None:
            return f"self: {id(self)} next: None"

        return f"self: {id(self)} next: {id(self.next)}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        self._i = None  # Used for iteration

    def add_at_start(self, value):
        old_head = self.head
        self.head = ListNode(value)
        self.head.next = old_head
        self.length += 1

    def add_at_end(self, value):
        if self.length == 0:
            self.head = ListNode(value)
            self.length += 1

        else:
            i = self.head
            while i != None:
                current_node = i
                i = i.next

            current_node.next = ListNode(value)
            self.length += 1

    def add_at(self, index, value):
        if index < 0 or index >= self.length:
            raise IndexError(
                f"Index out of Bound. Length of list {self.length}, index got to insert at {index}."
            )

        if index == 0:
            new_head = ListNode(value)
            new_head.next = self.head
            self.head = new_head
            self.length += 1

        else:
            i = 1
            running_node = self.head
            while i < index:
                running_node = running_node.next
                i += 1

            new_node = ListNode(value)
            new_node.next = running_node.next
            running_node.next = new_node
            self.length += 1

    def remove_at_start(self):
        if self.head == None:
            raise IndexError("No elements in list to remove.")

        node = self.head
        self.head = node.next
        self.length -= 1

        return node.value

    def remove_at_end(self):
        if self.head == None:
            raise IndexError("No elements in list to remove.")

        if self.length == 1:
            node = self.head
            self.head = None
            self.length -= 1

            return node.value

        else:
            i = self.head
            while i.next.next != None:
                i = i.next

            node = i.next
            i.next = None
            self.length -= 1

            return node.value

    def remove_at(self, index):
        if index < 0 or index >= self.length:
            raise IndexError(
                f"Index out of Bound. Length of list {self.length}, index got to insert at {index}."
            )

        if index == 0:
            node = self.head
            self.head = node.next
            self.length -= 1

            return node.value

        else:
            i = 1
            running_node = self.head
            while i < index:
                running_node = running_node.next
                i += 1

            node = running_node.next
            running_node.next = node.next
            self.length -= 1

            return node.value

    def __len__(self):
        return self.length

    def __iter__(self):
        self._i = self.head
        return self

    def __next__(self):
        if self._i != None:
            current_node = self._i
            self._i = self._i.next
            return current_node.value

        raise StopIteration

    def __getitem__(self, index):
        if index < 0 or index >= self.length:
            raise IndexError(
                f"Index out of Bound. Length of list {self.length}, index to get at is {index}."
            )

        node = self.head
        for i in range(index):
            node = node.next

        return node.value

    def __str__(self):
        result = "["

        for i in self:
            result += str(i) + ", "

        result += "]"

        return result

    def __repr__(self):
        result = "[\n"

        i = self.head
        while i != None:
            result += "\t" + str(i) + ",\n"
            i = i.next

        result += "]"

        return result


if __name__ == "__main__":
    # TODO: running tests or implement interactions
    ...
