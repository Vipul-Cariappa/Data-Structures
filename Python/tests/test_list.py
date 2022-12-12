from Python.LinkedList import LinkedList
from Python.CircularLinkedList import CircularLinkedList
from Python.DoublyLinkedList import DoublyLinkedList
from Python.CircularDoublyLinkedList import CircularDoublyLinkedList
import pytest


def test_lists():
    for listType in [
        LinkedList,
        CircularLinkedList,
        DoublyLinkedList,
        CircularDoublyLinkedList,
    ]:

        l1 = listType()
        l1.add_at_end(1)
        l1.add_at_end(2)
        l1.add_at_end(4)
        l1.add_at_end(5)
        l1.add_at_start(0)
        l1.add_at(3, 3)

        # testing len
        assert len(l1) == 6

        # testing str
        assert str(l1) == "[0, 1, 2, 3, 4, 5, ]"

        # testing iteration
        j = 0
        for i in l1:
            assert i == j
            j += 1

        # testing getitem
        assert l1[0] == 0
        assert l1[3] == 3
        assert l1[5] == 5

        # testing setitem
        l1[1] = -1
        l1[0] = -10
        l1[5] = 50

        assert l1.remove_at(1) == -1
        assert l1.remove_at_start() == -10
        assert l1.remove_at_end() == 50

        assert len(l1) == 3

        with pytest.raises(IndexError):
            tmp = l1[-1]

        with pytest.raises(IndexError):
            l1[3] = -1

        l2 = listType()
        l2.add_at_start(4)
        l2.add_at_start(2)
        l2.add_at_start(1)
        l2.add_at_end(5)
        l2.add_at(0, 0)
        l2.add_at(3, 3)

        # testing len
        assert len(l2) == 6

        # testing str
        assert str(l2) == "[0, 1, 2, 3, 4, 5, ]"

        # testing iteration
        j = 0
        for i in l2:
            assert i == j
            j += 1

        # testing getitem
        assert l2[0] == 0
        assert l2[3] == 3
        assert l2[5] == 5

        # testing setitem
        l2[0] = -1
        l2[1] = -2
        l2[4] = 40
        l2[5] = 50

        assert l2.remove_at(5) == 50
        assert l2.remove_at(0) == -1
        assert l2.remove_at_start() == -2
        assert l2.remove_at_end() == 40

        assert len(l2) == 2

        with pytest.raises(IndexError):
            l2.add_at(3, "error")

        l2.remove_at_end()
        l2.remove_at_end()

        assert len(l2) == 0

        l2.add_at_end(1)
        assert l2.remove_at_start() == 1

        assert len(l2) == 0

        with pytest.raises(IndexError):
            l2.add_at(3, "error")

        with pytest.raises(IndexError):
            l2.remove_at_end()

        with pytest.raises(IndexError):
            l2.remove_at_start()

        with pytest.raises(IndexError):
            l2.remove_at(0)

        with pytest.raises(IndexError):
            tmp = l2[0]

        with pytest.raises(IndexError):
            l2[0] = -1

        l3 = listType([1, 2, 3, 4])
        l3.add_at_start(0)
        l3.add_at_end(5)

        # testing len
        assert len(l3) == 6

        # testing str
        assert str(l3) == "[0, 1, 2, 3, 4, 5, ]"

        # testing iteration
        j = 0
        for i in l3:
            assert i == j
            j += 1

        if listType == DoublyLinkedList or listType == CircularDoublyLinkedList:
            j = 5
            for i in l3.backwards_iterator():
                assert j == i
                j -= 1

        # testing getitem
        assert l3[0] == 0
        assert l3[3] == 3
        assert l3[5] == 5

        # testing setitem
        l3[1] = -1
        l3[0] = -10
        l3[5] = 50

        assert l3.remove_at(1) == -1
        assert l3.remove_at_start() == -10
        assert l3.remove_at_end() == 50

        assert len(l3) == 3

        with pytest.raises(IndexError):
            tmp = l3[-1]

        with pytest.raises(IndexError):
            l3[3] = -1
