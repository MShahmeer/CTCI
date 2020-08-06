from __future__ import annotations
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

    def pop(self) -> Any:
        return self._items.pop()

    def is_empty(self) -> bool:
        return len(self._items) == 0


class Queue:
    _items = []

    def __init__(self) -> None:
        self._items = []

    def enqueue(self, item: Any) -> None:
        self._items.append(item)

    def dequeue(self) -> Any:
        return self._items.pop(0)

    def is_empty(self) -> bool:
        return len(self._items) == 0


class _GraphNode:
    item: Any
    adjacent: [_GraphNode]

    def __init__(self, item: Any) -> None:
        self.item = item
        self.adjacent = []

    def add_edge_to(self, destination: _GraphNode):
        self.adjacent.append(destination)

    def remove_edge_to(self, destination: _GraphNode):
        self.adjacent.remove(destination)


class Graph:
    _data: [_GraphNode]

    def __init__(self) -> None:
        self._data = []

    def find_node(self, item: Any) -> _GraphNode:
        for node in self._data:
            if node.item == item:
                return node

    def add_vertex(self, item: Any) -> None:
        self._data.append(_GraphNode(item))

    def add_edge(self, one: Any, two: Any) -> None:
        # Precondition: both one and two already exist as nodes in the graph
        first = self.find_node(one)
        second = self.find_node(two)
        first.add_edge_to(second)
        second.add_edge_to(first)

    def remove_vertex(self, item: Any) -> None:
        node_to_remove = self.find_node(item)
        adjacent = node_to_remove.adjacent
        for node in adjacent:
            node.remove_edge_to(node_to_remove)
        self._data.remove(node_to_remove)

    def remove_edge(self, one: Any, two: Any) -> None:
        first = self.find_node(one)
        second = self.find_node(two)
        first.remove_edge_to(second)
        second.remove_edge_to(first)

    def dfs(self, start: _GraphNode, end: _GraphNode, visited=[]) -> bool:
        # Returns true if there is a path between start and end using depth
        # first search
        if start not in visited:
            if start == end:
                return True
            visited.append(start)
            for neighbour in start.adjacent:
                if self.dfs(neighbour, end, visited):
                    return True
        return False

    def bfs(self, start: _GraphNode, end: _GraphNode) -> bool:
        # Returns true if there is a path between start and end using breadth
        # first search
        visited = []
        queue = Queue()
        queue.enqueue(start)
        while not queue.is_empty():
            node = queue.dequeue()
            if node == end:
                return True
            visited.append(node)
            for neighbour in node.adjacent:
                if neighbour not in visited:
                    queue.enqueue(neighbour)
        return False
