from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)

  def create_arr(self, size):
    ''' This method creates an array of Linked Lists based on the size of the Hash Table '''
    arr = []
    for _ in range(size):
      new_ll = LinkedList()
      arr.append(new_ll)
    
    return arr 

  def hash_func(self, key):
    ''' This Hash Function determines the position based on the ascii value of the first character in the key '''
    first_letter = key[0]
    ascii_value = ord(first_letter)
    index = ascii_value % self.size

    return index

  def insert(self, key, value):
    ''' Inserts a node into the Hash Table '''
    new_data = (key, value)
    index = self.hash_func(key)

    ll = self.arr[index]
    found_node = ll.find(key)

    if found_node == -1:
      ll.append(new_data)
    else:
      ll.update(key, value)

  def print_key_values(self):
    ''' Prints the key value pairs of each linked list in the Hash Table '''
    for ll in self.arr:
      ll.print_nodes()



