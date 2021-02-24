from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)

  def create_arr(self, size):
    arr = []
    for _ in range(size):
      new_ll = LinkedList()
      arr.append(new_ll)
    
    return arr 

  def hash_func(self, key):
    first_letter = key[0]
    ascii_value = ord(first_letter)
    index = ascii_value % self.size

    return index


  # 3️⃣ TODO: Complete the insert method.

  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

  def insert(self, key, value):
    
    new_data = (key, value)
    index = self.hash_func(key)

    ll = self.arr[index]
    found_node = ll.find(key)

    if found_node == -1:
      ll.append(new_data)
    else:
      ll.update(key, value)


  
    # Only append new node if the key is not in HashTable
    # Otherwise, if the word is already in the table, dont create new node, just udpate vvalue




  # 4️⃣ TODO: Complete the print_key_values method.

  # Traverse through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  #See linked list.py, print_nodes function

  def print_key_values(self):
    for ll in self.arr:
      ll.print_nodes()



