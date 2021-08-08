from typing import Generic, TypeVar


T = TypeVar("T")


class Queue(Generic[T]):
    def __init__(self) -> None:
        self.front = None
        self.end = None
        self.size = 0

    def add(self, data: T) -> None:
        node = QueueNode(data)
        if self.end:
            self.end.next = node
        self.end = node

        if self.front == None:
            self.front = self.end

        self.size += 1

    def remove(self) -> T:
        if self.empty() == True:
            return None

        data = self.peek()
        self.front = self.front.next
        if self.front == None:
            self.end = None
        self.size -= 1
        return data

    def peek(self) -> T:
        return None if self.empty() == True else self.front.data

    def get_size(self) -> int:
        return self.size

    def empty(self) -> bool:
        return self.size == 0
    
    def __str__(self) -> str:
        result = ""
        front = self.front
        while front != None:
            result += front.data
            if front.next != None:
                result += ", "
            front = front.next
        return result


class QueueNode(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data = data
        self.next = None
