import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    new_item = item
    self.storage.add_to_tail(new_item)
    self.size += 1
  
  def dequeue(self):
    if self.size > 0:
      self.size -= 1
    return self.storage.remove_head()

  def len(self):
    return self.size
