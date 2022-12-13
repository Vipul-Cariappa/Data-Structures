import pytest
from Python.Stack import Stack
from Python.Queue import Queue


def test_stack():
    s1 = Stack()

    with pytest.raises(IndexError):
        s1.pop()

    with pytest.raises(IndexError):
        s1.peek()

    s1.push(1)
    s1.push(2)
    s1.push(3)

    assert len(s1) == 3

    assert s1.peek() == 3
    assert s1.pop() == 3

    assert s1.peek() == 2
    assert s1.pop() == 2

    assert s1.peek() == 1
    assert s1.pop() == 1

    with pytest.raises(IndexError):
        s1.pop()

    with pytest.raises(IndexError):
        s1.peek()

    # testing string conversion
    s2 = Stack()
    assert str(s2) == "+---+"

    s2.push(1)
    assert str(s2) == "+---+\n| 1 |\n+---+\n"


def test_Queue():
    q1 = Queue()

    with pytest.raises(IndexError):
        q1.dequeue()

    with pytest.raises(IndexError):
        q1.peek()

    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)

    assert len(q1) == 3

    assert q1.peek() == 1
    assert q1.dequeue() == 1

    assert q1.peek() == 2
    assert q1.dequeue() == 2

    assert q1.peek() == 3
    assert q1.dequeue() == 3

    with pytest.raises(IndexError):
        q1.dequeue()

    with pytest.raises(IndexError):
        q1.peek()
