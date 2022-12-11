class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    # def __str__(self):
    #     if self.next is None:
    #         return f"self: {id(self)} next: None"

    #     return f"self: {id(self)} next: {id(self.next)}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_at_start(self, value):
        old_head = self.head
        self.head = ListNode(value)
        self.head.next = old_head

        if self.length == 0:
            self.tail = self.head

        self.length += 1

    def add_at_end(self, value):
        if self.length == 0:
            self.head = ListNode(value)
            self.tail = self.head
            self.length += 1
            return

        self.tail.next = ListNode(value)
        self.tail = self.tail.next
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
            return

        running_node = self.head
        for _ in range(index - 1):
            running_node = running_node.next

        new_node = ListNode(value)
        new_node.next = running_node.next
        running_node.next = new_node
        self.length += 1

    def remove_at_start(self):
        if self.length == 0:
            raise IndexError("No elements in list to remove.")

        node = self.head
        self.head = node.next

        self.length -= 1
        if self.length == 0:
            self.tail = None

        return node.value

    def remove_at_end(self):
        # time complexity is O(n)
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
        if index < 0 or index >= self.length:
            raise IndexError(
                f"Index out of Bound. Length of list {self.length}, index got to insert at {index}."
            )

        if index == 0:
            node = self.head
            self.head = node.next
            self.length -= 1
            return node.value

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
        running_node = self.head
        while running_node is not None:
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

    # def __repr__(self):
    #     result = "[\n"

    #     i = self.head
    #     while i is not None:
    #         result += "\t" + str(i) + ",\n"
    #         i = i.next

    #     result += "]"

    #     return result


if __name__ == "__main__":
    ...
