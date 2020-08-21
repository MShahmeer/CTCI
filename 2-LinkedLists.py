"""
DOCTESTS:
"""

from DataStructures import _Node, LinkedList

"""
Problem 8 - Loop Detection:
Given a circular linked list, implement an algorithm that returns the node at
the beginning of the loop.

Time complexity: O(n), space complexity: O(n)
"""


def loop_detection(lst: LinkedList) -> _Node:
    encountered = []
    curr = lst._first
    while curr not in encountered:
        encountered.append(curr)
        curr = curr.next
    return curr
