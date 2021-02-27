class Vertex:
  def __init__(self, id):
    self.id = id
    self.neighbors = {}

  def get_id(self):
    return self.id

  def add_neighbors(self, neighbor_id, weight=0):
    self.neighbors[neighbor_id] = weight

  def get_neighbors(self):
    return self.neighbors.keys

  def get_weight(self, neighbor_id):
    return self.neighbors[neighbor_id]
