from Vertex import Vertex

class Graph:

  def __init__(self):
    self.vertices = {}

  def add_vertex(self, id):
    new_vertex = Vertex(id)
    self.vertices[id] = new_vertex
    return new_vertex

  def get_vertices(self):
    return self.vertices.keys()

  def get_vertex(self, id):
    if id in self.vertices:
      return self.vertices[id]
    else:
      return None

  def add_edge(self, start_id, end_id, weight=0):
    if start_id not in self.vertices:
      start_vertex = self.add_vertex(start_id)
    if end_id not in self.vertices:
      end_vertex = self.add_vertex(end_id)

    self.vertices[start_id].add_neighbors(end_id, weight)