from Node import Node

class LinkedList:

  def __init__(self):
    self.head = None


  def append(self, new_data):
    ''' Append method that will add a new Node to the beginning of the Linked List '''
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node


  def find(self,item):
    '''Find method to find a Node on the given key '''
    current = self.head
    found = False
    counter = 0

    while current != None and not found:
      if current.data[0] == item:
        found = True
      else:
        current = current.next
        counter += 1

    if found:
      return counter
    else:
      return -1

  def update(self, key, value):
    ''' Update method that finds the key, and updates the value '''
    current = self.head
    found = False
    counter = 0

    while current != None and not found:
      if current.data[0] == key:
        current.data = (current.data[0], current.data[1] + 1)
        found = True
      else:
        current = current.next
        counter += 1

  def length(self):
    ''' This method returns the length of the linked list '''
    if self.head == None:
      return 0
    else:
      counter = 1
      current = self.head
      while(current.next):
        current = current.next
        counter +=1
      return counter


  def print_nodes(self):
    ''' This will print the nodes in the Linked List { key : value } '''
    current = self.head
    
    if current == None:
      pass
    else:
      for i in range(self.length()):
        print(f'{current.data[0]} : {current.data[1]}')
        current = current.next