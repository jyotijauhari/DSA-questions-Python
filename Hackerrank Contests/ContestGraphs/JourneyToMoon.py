class Vertex:

    def __init__(self, value):
        self.value = value
        self.neighbours = []


class Graph:

    def __init__(self):
        self.vertices = {}

    def create_vertex(self, value):
        if value not in self.vertices:
            vertex = Vertex(value)
            self.vertices[value] = vertex


    def create_edge(self, first, second):

        if (first in self.vertices) and (second in self.vertices):
            vfirst = self.vertices[first]
            vsecond = self.vertices[second]

            vfirst.neighbours.append(vsecond)
            vsecond.neighbours.append(vfirst)

    def display(self):
        for vertex in self.vertices.values():
            print(vertex.value, end=" => ")
            print(", ".join([neighbour.value for neighbour in vertex.neighbours]))

    def connected_components(self):
        components = []
        stack = []
        to_process = set()

        for start in self.vertices.values():
            if start in to_process:
                continue

            component = []
            stack.append(start)
            to_process.add(start)

            while len(stack) > 0:
                top = stack.pop()

                component.append(top.value)
                for neighbour in top.neighbours:
                    if neighbour not in to_process:
                        stack.append(neighbour)
                        to_process.add(neighbour)

            components.append(component)

        return components

N,P = list(map(int,input().strip().split(' ')))
graph = Graph()

for i in range(N):
    graph.create_vertex(i)

for j in range(P):
    u,v = list(map(int,input().strip().split(' ')))
    graph.create_edge(u,v)
    graph.create_edge(v,u)

initial_total = (N*(N-1))//2

temp_list = (graph.connected_components())
total = 0
for i in range(len(temp_list)):
    n = len(temp_list[i])
    total += (n*(n-1))//2

final_total = initial_total - total
print(final_total)
