class LinkedList:
  def __init__(self):
    self.head = None
    self.size = 0
  
  def add(self, data):
    node = LinkedListNode(data)
    node.next = self.head
    self.head = node
    self.size += 1

  def get_size(self):
    return self.size

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
  def __init__(self, data):
    self.data = data
    self.next = None