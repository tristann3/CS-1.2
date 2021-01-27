from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None

  def add_song(self, title):
    '''Adds song to the Playlist and reassigns the head of the linked list'''
    new_song = Song(title)
    new_song.set_title(title)
    new_song.set_next_song(self.__first_song)
    self.__first_song = new_song

  def find_song(self, title):
    '''Finds song in the linked list by traversing the .next of each song/node'''
    counter = 0
    current_song = self.__first_song

    while (current_song.get_title().lower() != title.lower()):
      # if the end of the linked list is reached, return -1, meaning nothing was found
      if current_song.get_next_song == None:
        return -1
      current_song = current_song.get_next_song()
      counter += 1
    print(f"Found the song {current_song.get_title()}")
    return counter 

  def remove_song(self, title):
    '''Removes the song from the playlist by updating the next node that the previous node points to'''
    current_song = self.__first_song

    # this use case for when a linked list has only one entry, or it is at the end of the list
    if (current_song.get_title() == title.title()):
      self.__first_song = current_song.get_next_song()
      print(f'{current_song.get_title()} has been removed!')
      return

    # while the current song's next node is not title, pass
    while(current_song.get_next_song() != None):
      # general case -> has more than 2 nodes after
      if (current_song.get_next_song().get_title() == title.title()):
        current_song.set_next_song(current_song.get_next_song().get_next_song())
        print(f'{title.title()} has been removed!')
        return

      current_song = current_song.get_next_song()

  def length(self):
    '''Function that returns the length of the Linked List'''
    counter = 0
    current_song = self.__first_song

    while current_song != None:
      counter += 1
      current_song = current_song.get_next_song()

    return counter

  def print_songs(self):
    '''Dynamically Prints all Songs in the Playlist'''
    current_song = self.__first_song
    counter = 1

    while current_song != None:
      print(f'{counter}. {current_song.get_title()}')
      current_song = current_song.get_next_song()
      counter += 1
