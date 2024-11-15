from __future__ import annotations
from typing import Optional, Any
from dataclasses import dataclass


@dataclass
class Node:
    data: Any
    next: Optional[Node] = None


class LinkedList:
    def __init__(self):
        self.head = Node(None)

    def __repr__(self):
        temp: Node = self.head
        result: str = "head "
        while temp.next:
            temp = temp.next
            result += f"-> {temp.data} "
        return result

    def __eq__(self, other):
        if not isinstance(other, LinkedList):
            raise NotImplementedError

        self_temp: Node = self.head
        other_temp: Node = other.head
        while self_temp and other_temp:
            if self_temp.data != other_temp.data:
                return False
            self_temp = self_temp.next
            other_temp = other_temp.next

        if not self_temp or not other_temp:  # One is longer than the other
            return False

        return True

    def push_front(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node

    def push_back(self, data: Any) -> None:
        new_node = Node(data)

        if not self.head:
            self.head.next = new_node
            return

        temp: Node = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    def insert(self, data: Any, position: int) -> None:
        if position < 1:
            raise IndexError("Position should be >= 1.")

        if position == 1:
            self.push_front(data)
            return

        new_node: Node = Node(data)
        temp: Node = self.head

        for i in range(1, position):
            if temp.next:
                temp = temp.next
            else:
                raise IndexError("Position out of range")

        new_node.next = temp.next
        temp.next = new_node

    def pop_front(self) -> None:
        if not self.head.next:
            return

        self.head.next = self.head.next.next

    def pop_back(self) -> None:
        if not self.head.next:
            return

        temp = self.head

        if not temp.next.next:
            temp.next = None
            return

        while temp.next.next:
            temp = temp.next

        temp.next = None

    def delete(self, position: int) -> None:
        if position < 1:
            raise IndexError("Position should be >= 1.")

        if position == 1:
            self.pop_front()
            return

        temp: Node = self.head

        for i in range(1, position):
            if temp.next:
                temp = temp.next
            else:
                raise IndexError("Position out of range")

        temp.next = temp.next.next if temp.next else None
