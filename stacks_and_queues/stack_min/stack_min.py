"""
Stack Min

How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop
and min should all operate in O(1) time.
"""

# Time: O(1) for push, pop, and min
# Save the minimum of the stack for each node when it's at the top.
class Stack:
  def __init__(self) -> None:
    self.top = None
  
  def push(self, data: int) -> None:
    node = None
    if self.empty() or data < self.min():
      node = _Node(data, data)
    else:
      node = _Node(data, self.min())

    node.next = self.top
    self.top = node
  
  def pop(self) -> int:
    if self.empty():
      return None
    
    data = self.peek()
    self.top = self.top.next
    return data
  
  def min(self) -> int:
    if self.empty():
      return None
    
    return self.top.min
  
  def peek(self) -> int:
    if self.empty():
      return None
    
    return self.top.data

  def empty(self) -> bool:
    return self.top == None


class _Node:
  def __init__(self, data: int, min: int) -> None:
    self.data = data
    self.next = None
    self.min = min