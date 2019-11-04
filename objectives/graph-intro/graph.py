class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id is not None:
            self.vertices[vertex_id] = self.vertices[vertex_id] or set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise KeyError("Vertex does not exist")