from queue import Queue
from stack import Stack


class Graph:
    def __init__(self):
        self.vertices = {}

    def __str__(self):
        return f"{self.vertices}"

    def add_vertex(self, vertex_id):
        if vertex_id is not None:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise KeyError("Vertex does not exist")

    def breath_first_traversal(self, starting_vertex_id):
        # Instantiate queue and enqueue the starting vertex ID
        queue = Queue()
        queue.enqueue(starting_vertex_id)

        # store visited vertices
        visited = set()

        # loop over vertices while queue not empty
        while queue.length() > 0:
            # dequeue the first vertex
            vertex = queue.dequeue()

            # if current vertex has not been visited
            if vertex not in visited:
                # mark it as visited by printing it out
                # print(vertex)
                visited.add(vertex)

                # add all other neighbor to the back of the queue
                for next_vertex in self.vertices[vertex]:
                    queue.enqueue(next_vertex)

    def dept_first_traversal(self, start_index_id):
        # Create new stack and push in starting index
        stack = Stack()
        stack.push(start_index_id)

        # Store visited vertices
        visited = set()

        while stack.length() > 0:
            # remove the first vertex
            vertex = stack.pop()

            # check if current vertex has not been visited
            if vertex not in visited:
                # mark as visited by add it to visited and printing it out
                # print(vertex)
                visited.add(vertex)

                # Add all of it's neighbor's to the top of the stack
                for next_vertex in self.vertices[vertex]:
                    stack.push(next_vertex)


graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')

graph.add_edge('0', '1')
graph.add_edge('0', '3')
# graph.add_edge('0', '4')
# print(graph.breath_first_traversal('0'))
# print(graph)
graph.dept_first_traversal('0')
