from typing import Generic, TypeVar, List


T = TypeVar('T')


class LinkedList(Generic[T]):
    def __init__(self, arr: List[T]=None) -> None:
        self.head = None
        self.tail = None
        self.size = 0
        if arr != None:
            for i in arr:
                self.add(i)
    
    def add(self, data: T) -> None:
        self.size += 1

        node = LinkedListNode(data)
        if self.tail != None:
            self.tail.next = node
        self.tail = node

        if self.head == None:
            self.head = self.tail

    def add_left(self, data: T) -> None:
        self.size += 1

        node = LinkedListNode(data)
        node.next = self.head
        self.head = node

        if self.tail == None:
            self.tail = self.head

    def get_size(self) -> int:
        return self.size
    
    def __str__(self) -> str:
        result = ""
        node = self.head
        while node != None:
            result += str(node.data)
            if node.next != None:
                result += ", "
            node = node.next
        return result


class LinkedListNode(Generic[T]):
    def __init__(self, data) -> None:
        self.data = data
        self.next = None