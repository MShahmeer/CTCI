"""
DOCTESTS:

Problem 8:
>>> lst = LinkedList()
>>> node1 = _Node("A")
>>> node2 = _Node("B")
>>> node3 = _Node("C")
>>> node4 = _Node("D")
>>> node5 = _Node("E")
>>> node5.next = node3
>>> node4.next = node5
>>> node3.next = node4
>>> node2.next = node3
>>> node1.next = node2
>>> lst._first = node1
>>> loop_detection(lst)
Node3
"""

"""
Problem 8 - Loop Detection:
Given a circular linked list, implement an algorithm that returns the node at
the beginning of the loop.

Time complexity: O(n), space complexity: O(n)
"""

from DataStructures import _Node, LinkedList


def loop_detection(lst: LinkedList) -> _Node:
    encountered = []
    curr = lst._first
    while curr not in encountered:
        encountered.append(curr)
        curr = curr.next
    return curr


lst = LinkedList()
node1 = _Node("A")
node2 = _Node("B")
node3 = _Node("C")
node4 = _Node("D")
node5 = _Node("E")
node5.next = node3
node4.next = node5
node3.next = node4
node2.next = node3
node1.next = node2
lst._first = node1
print(loop_detection(lst).item)
