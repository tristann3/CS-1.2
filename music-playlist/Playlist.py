from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    new_song = Song(title)
    new_song.set_next_song(self.__first_song)
    self.__first_song = new_song



  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    counter = 0
    current_song = self.__first_song

    while (current_song.get_title().lower() != title.lower()):
      # if the end of the linked list is reached, return -1
      if current_song.get_next_song == None:
        return -1
      current_song = current_song.get_next_song()
      counter += 1
    print(f"Found the song {current_song.get_title()}")
    return counter 



  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    current_song = self.__first_song

    # this use case for when a linked list has only one entry, or it is at the end of the list
    if (current_song.get_title() == title):
      self.__first_song = current_song.get_next_song()
      return

    # while the current song's next node is not title, pass
    while(current_song.get_next_song() != None):
      print(current_song.get_title())

      # general case -> has more than 2 nodes after
      if (current_song.get_next_song().get_title() == title):
        current_song.set_next_song(current_song.get_next_song().get_next_song())
        return

      # this use case is for when the song is the first item in a list


      current_song = current_song.get_next_song()



  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    counter = 0
    current_song = self.__first_song

    while current_song != None:
      counter += 1
      current_song = current_song.get_next_song()

    return counter


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    current_song = self.__first_song
    counter = 1
    while current_song != None:
      print(f'{counter}. {current_song.get_title()}')
      current_song = current_song.get_next_song()
      counter += 1

  