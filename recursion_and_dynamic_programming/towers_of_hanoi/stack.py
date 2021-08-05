from typing import TypeVar


T = TypeVar('T')


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.size = 0
    
    def push(self, data: T) -> None:
        node = StackNode(data)
        node.next = self.top
        self.top = node

        self.size += 1
    
    def pop(self) -> T:
        if self.empty() == True:
            return None
        data = self.top.data
        self.top = self.top.next

        self.size -= 1
        return data

    def peek(self) -> T:
        if self.empty() == True:
            return None
        return self.top.data
    
    def get_size(self) -> int:
        return self.size

    def empty(self) -> bool:
        return self.size == 0


class StackNode:
    def __init__(self, data: T) -> None:
        self.data = data
        self.next = None