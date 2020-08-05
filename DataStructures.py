from typing import Optional, Any


class _Node:
    item: Any
    next: Optional[_Node]

    def __init__(self, item: Any) -> None:
        self.item = item
        self.next = None


class LinkedList:
    _first: Optional[_Node]

    def __init__(self) -> None:
        self._first = None

    def insert(self, item: Any) -> None:
        node = _Node(item)
        if self._first is None:
            self._first = node
        else:
            curr = self._first
            while curr.next is not None:
                curr = curr.next
            curr.next = node

    def remove(self) -> None:
        if self._first is None:
            return
        curr = self._first
        while curr.next is not None:
            curr = curr.next
        curr.next = None


class Stack:
    _items = []

    def __init__(self) -> None:
        self._items = []

    def push(self, item: Any) -> None:
        self._items.append(item)

    def pop(self, item: Any) -> None:
        self._items.pop(item)


class Queue:
    _items = []

    def __init__(self) -> None:
        self._items = []

    def push(self, item: Any) -> None:
        self._items.append(item)

    def pop(self, item: Any) -> None:
        self._items.pop(item, 0)


class Graph:
    _data: {Any: [Any]}

    def __init__(self) -> None:
        self._data = {}

    def add_vertex(self, item: Any) -> None:
        self._data[item] = []

    def add_edge(self, one: Any, two: Any) -> None:
        self._data[one].append(two)
        self._data[two].append(one)

    def remove_vertex(self, item: Any) -> None:
        self._data.pop(item)
        for vertex in self._data:
            if item in self._data[vertex]:
                self._data[vertex].remove(item)

    def remove_edge(self, one: Any, two: Any) -> None:
        self._data[one].remove(two)
        self._data[two].remove(one)
