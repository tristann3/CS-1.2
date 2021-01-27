class Song:

  def __init__(self, title):
      self.__title = title
      self.__next_song = None


  def get_title(self):
    '''Getter for song title'''
    return self.__title
  
  def set_title(self, title):
    '''Setter for song title'''
    title = str(title)
    title = title.title()
    print(title)
    
    self.__next_song = title

  def get_next_song(self):
    '''Getter for next node/song in the linked list'''
    return self.__next_song

  def set_next_song(self, next_song):
    '''Setter for the next node//song in the linked list'''
    self.__next_song = next_song

  def __str__(self):
    '''Dunder str method to return the song title'''
    return f'{self.__title}'

  def __repr__(self):
    '''Dunder repr method to show the next node that this song points to'''
    return f'{self.__title} -> {self.__next_song}'