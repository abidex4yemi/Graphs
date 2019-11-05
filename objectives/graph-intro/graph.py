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

    def dft_recursive(self, start_vert, visited=None):
        # if the visited structure is set to None
        if visited is None:
            # create a new set for visited
            visited = set()

        # add a starting vertex to the visited set
        visited.add(start_vert)
        # print the start vertex
        print(start_vert)
        # loop over every child vertex in vertices set at the start vertex
        for child_vert in self.vertices[start_vert]:
            # if child vertex is not in visited
            if child_vert not in visited:
                # do a recursive call to dft_recursive
                # using the child vertex and the current
                #  visited set as arguments
                self.dft_recursive(child_vert, visited)

    def dfs(self, start_vert, target_value, visited=None):
        # if visited is None
        if visited is None:
            # create a new set of visited
            visited = set()
        # add start vert to visited
        visited.add(start_vert)
        # if the start vert is equal to the target value
        if start_vert == target_value:
            # return True
            return True
        # loop over every child vertex in vertices set at the start vertex
        for child_vert in self.vertices[start_vert]:
            # if child vert is not in visited
            if child_vert not in visited:
                # if the recursive call to dfs
                if self.dfs(child_vert, target_value, visited):
                    # return True
                    return True
        # Return False
        return False

    def bfs(self, starting_vertex_id, target_value):
        # create a queue to hold the vertex ids
        q = Queue()
        # enqueue the start vertex id
        q.enqueue(starting_vertex_id)
        # create an empty visited set
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # set vert to the dequeued element
            vert = q.dequeue()
            # if the vert is not in visited
            if vert not in visited:
                # if vert is target value
                if vert == target_value:
                    # return True
                    return True
                # add the vert to visited set
                visited.add(vert)
                # loop over next vert in the vertices at the index of vert
                for next_vert in self.vertices[vert]:
                    # enqueue the next vert
                    q.enqueue(next_vert)
        # return False
        return False

    def bfs_path(self, starting_vertex_id, target_value):
        # create a queue
        q = Queue()
        # enqueue a list holding the starting vertex id
        q.enqueue([starting_vertex_id])
        # created an empty visited set
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # dequeue to the path
            path = q.dequeue()
            # set a vert to the last item in the path
            vert = path[-1]
            # if vert is not in visited
            if vert not in visited:
                # if vert is equal to target value
                if vert == target_value:
                    # return path
                    return path
                # add vert to visited set
                visited.add(vert)
                # loop over next vert in vertices at the index of vert
                for next_vert in self.vertices[vert]:
                    # set a new path equal to a new list of the path (copy)
                    new_path = list(path)
                    # append next vert to new path
                    new_path.append(next_vert)
                    # enqueue the new path
                    q.enqueue(new_path)
        # return None
        return None

    def dfs_path(self, starting_vertex_id, target_value):
        # create a stack
        s = Stack()
        # push a list holding the starting vertex id
        s.push([starting_vertex_id])
        # created an empty visited set
        visited = set()
        # while the queue is not empty
        while s.size() > 0:
            # pop to the path
            path = s.pop()
            # set a vert to the last item in the path
            vert = path[-1]
            # if vert is not in visited
            if vert not in visited:
                # if vert is equal to target value
                if vert == target_value:
                    # return path
                    return path
                # add vert to visited set
                visited.add(vert)
                # loop over next vert in vertices at the index of vert
                for next_vert in self.vertices[vert]:
                    # set a new path equal to a new list of the path (copy)
                    new_path = list(path)
                    # append next vert to new path
                    new_path.append(next_vert)
                    # push the new path
                    s.push(new_path)
        # return None
        return None


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
# graph.dept_first_traversal('0')

graph.dft_recursive('0')
