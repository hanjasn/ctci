from typing import Generic, TypeVar


T = TypeVar('T')


class Stack(Generic[T]):
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
        
        data = self.peek()
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self) -> T:
        return None if self.empty() == True else self.top.data
    
    def get_size(self) -> int:
        return self.size

    def empty(self) -> bool:
        return self.size == 0
    
    def __str__(self) -> str:
        result = ""
        top = self.top
        while top != None:
            result += top.data
            if top.next != None:
                result += ", "
            top = top.next
        return result


class StackNode(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data = data
        self.next = None