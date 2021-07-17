"""
Stack of Plates

Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start
a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks
should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and
SetOfStacks.pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there
were just a single stack).

Follow Up:
Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
"""
from typing import TypeVar
from stack import Stack


T = TypeVar('T')


# Time: All in O(1) time (except print_values)
class SetOfStacks:
  def __init__(self, capacity: int) -> None:
    self.stacks = []
    self.capacity = capacity
  
  def push(self, data: T) -> None:
    if self.is_empty() or self.is_last_stack_full():
      self.stacks.append(Stack())
    self.get_last_stack().push(data)

  def pop(self) -> T:
    if self.is_empty():
      return None
    
    data = self.peek()
    self.get_last_stack().pop()
    if self.get_last_stack().is_empty():
      self.stacks.pop()
    return data
  
  def pop_at(self, index: int) -> T:
    if self.is_empty() or index == len(self.stacks) - 1:
      return self.pop()

    data = self.stacks[index].peek()
    self.stacks[index].pop()

    for i in range(index, len(self.stacks) - 1):
      bottom = self.stacks[i + 1].remove_bottom()
      self.stacks[i].push(bottom)

    return data
  
  def peek(self) -> T:
    return self.get_last_stack().peek()

  def is_empty(self) -> bool:
    return len(self.stacks) == 0
  
  def is_last_stack_full(self) -> bool:
    if self.is_empty():
      return False

    return self.get_last_stack().get_size() == self.capacity
  
  def get_last_stack(self) -> Stack:
    if self.is_empty():
      return None

    return self.stacks[-1]

  def print_values(self) -> str:
    result = ""
    for i in range(len(self.stacks) - 1, -1, -1):
      if i == 0:
        result += self.stacks[i].print_values()
      else:
        result += self.stacks[i].print_values() + " | "
    return result