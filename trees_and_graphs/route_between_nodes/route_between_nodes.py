"""
Route Between Nodes

Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
"""
from queue import Queue
from typing import TypeVar


T = TypeVar('T')


class Graph:
  def __init__(self, directed: bool=False) -> None:
    self.graph = dict()
    self.directed = directed

  def add_vertex(self, vertex: T) -> None:
    if vertex in self.graph:
      return
    
    self.graph[vertex] = set()

  def add_edge(self, vertex1: T, vertex2: T) -> None:
    if vertex1 not in self.graph:
      self.add_vertex(vertex1)
    if vertex2 not in self.graph:
      self.add_vertex(vertex2)
    
    self.graph[vertex1].add(vertex2)
    if not self.directed:
      self.graph[vertex2].add(vertex1)

  def remove_vertex(self, vertex: T) -> None:
    if vertex not in self.graph:
      return
    
    if not self.directed:
      for child in self.graph[vertex]:
        self.graph[child].discard(vertex)
    else:
      for children in self.graph.values():
        children.discard(vertex)
    self.graph.pop(vertex)

  def remove_edge(self, vertex1: T, vertex2: T) -> None:
    if vertex1 not in self.graph or vertex2 not in self.graph:
      return
    
    self.graph[vertex1].discard(vertex2)
    if not self.directed:
      self.graph[vertex2].discard(vertex1)
  
  def path_exists(self, vertex1: T, vertex2: T) -> bool:
    if vertex1 not in self.graph or vertex2 not in self.graph:
      return False
    
    visited = dict()
    for vertex in self.graph:
      visited[vertex] = False
    queue = Queue()
    queue.put(vertex1)
    visited[vertex1] = True
    while not queue.empty():
      vertex = queue.get()
      for child in self.graph[vertex]:
        if not visited[child]:
          if child == vertex2:
            return True
          visited[child] = True
          queue.put(child)
    return False
  
  def __str__(self) -> str:
    result = ""
    i = 1
    for vertex in self.graph:
      children = ""
      for child in self.graph[vertex]:
        children += f'{str(child)}, '
      
      if i == len(self.graph):
        result += f'{vertex}: {children}'
      else:
        result += f'{vertex}: {children}\n'
      i += 1
    return result