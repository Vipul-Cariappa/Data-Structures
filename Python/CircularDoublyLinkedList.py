class DListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        if self.next == None and self.previous == None:
            return f"previous: None self: {id(self)} next: None"

        elif self.next == None:
            return f"previous: {id(self.previous)} self: {id(self)} next: None"

        elif self.previous == None:
            return f"previous: None self: {id(self)} next: {id(self.next)}"

        return f"previous: {id(self.previous)} self: {id(self)} next: {id(self.next)}"


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self._i = None  # Used for iteration
        self._index = 0  # Used for iteration

    def add_at_start(self, value):
        old_head = self.head
        self.head = DListNode(value)
        self.head.next = old_head if old_head != None else self.head
        self.head.previous = self.tail if self.tail != None else self.head
        if old_head != None:
            old_head.previous = self.head

        if self.tail == None:
            self.tail = self.head
        else:
            self.tail.next = self.head

        self.length += 1

    def add_at_end(self, value):
        if self.length == 0:
            self.head = DListNode(value)
            self.head.next = self.head
            self.head.previous = self.head
            self.tail = self.head
            self.length += 1

        else:
            i = self.head
            for _ in range(self.length):
                current_node = i
                i = i.next

            current_node.next = DListNode(value)
            current_node.next.previous = current_node
            self.tail = current_node.next
            self.head.previous = current_node.next
            current_node.next.next = self.head
            self.length += 1

    def add_at(self, index, value):
        if index < 0 or index >= self.length:
            raise IndexError(
                f"Index out of Bound. Length of list {self.length}, index got to insert at {index}."
            )

        if index == 0:
            new_head = DListNode(value)
            new_head.previous = self.tail
            new_head.next = self.head
            self.head.previous = new_head
            self.head = new_head
            self.tail.next = self.head
            self.length += 1

        else:
            i = 1
            running_node = self.head
            while i < index:
                running_node = running_node.next
                i += 1

            new_node = DListNode(value)
            new_node.next = running_node.next
            new_node.previous = running_node
            new_node.next.previous = new_node
            running_node.next = new_node
            self.length += 1

    def remove_at_start(self):
        if self.head == None:
            raise IndexError("No elements in list to remove.")

        if self.length == 1:
            node = self.head
            self.head = None
            self.tail = None

            return node.value

        node = self.head
        self.head = node.next
        self.head.previous = self.tail if self.tail != None else self.head
        if self.tail != None:
            self.tail.next = self.head
        else:
            self.tail = self.head

        self.length -= 1

        return node.value

    def remove_at_end(self):
        if self.head == None:
            raise IndexError("No elements in list to remove.")

        if self.length == 1:
            node = self.head
            self.head = None
            self.tail = None
            self.length -= 1

            return node.value

        else:
            i = self.head
            for _ in range(self.length - 1):
                current_node = i
                i = i.next

            node = current_node.next
            current_node.next = self.head
            self.tail = current_node
            self.length -= 1

            return node.value

    def remove_at(self, index):
        if index < 0 or index >= self.length:
            raise IndexError(
                f"Index out of Bound. Length of list {self.length}, index got to insert at {index}."
            )

        if self.length == 1:
            node = self.head
            self.head = None
            self.tail = None

            return node.value

        if index == 0:
            node = self.head
            self.head = node.next
            self.head.previous = self.tail
            self.tail.next = self.head
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
            node.next.previous = running_node
            self.length -= 1

            return node.value

    def __len__(self):
        return self.length

    def __iter__(self):
        self._i = self.head
        self._index = 0
        return self

    def __next__(self):
        if self._index < self.length:
            self._index += 1
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
        for _ in range(self.length):
            result += "\t" + str(i) + ",\n"
            i = i.next

        result += "]"

        return result


if __name__ == "__main__":
    # TODO: running tests or implement interactions
    ...
