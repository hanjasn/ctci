class LinkedList:
  def __init__(self) -> None:
      self.head = None

  def add(self, data):
    node = LinkedListNode(data)
    node.next = self.head
    self.head = node
  
  def print_list(self):
    node = self.head
    result = ""
    while node != None:
      if node.next == None:
        result += str(node.data)
      else:
        result += str(node.data) + ", "
      node = node.next
    return result


class LinkedListNode:
  def __init__(self, data) -> None:
      self.data = data
      self.next = None