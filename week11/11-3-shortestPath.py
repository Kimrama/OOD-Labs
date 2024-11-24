class Graph:
    def __init__(self):
        self.edges = {} 

    def add_edge(self, u, v, weight):
        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:  
            self.edges[v] = []
        self.edges[u].append((v, weight))

    def dijkstra(self, start, target):
        if start not in self.edges or target not in self.edges:
            return None

        shortest_paths = {vertex: float('inf') for vertex in self.edges}
        shortest_paths[start] = 0
        previous_vertices = {vertex: None for vertex in self.edges}
        unvisited = list(self.edges.keys())

        while unvisited:
            current_vertex = min(unvisited, key=lambda vertex: shortest_paths[vertex])

            if shortest_paths[current_vertex] == float('inf'):
                break
            if current_vertex == target:
                break

            unvisited.remove(current_vertex)

            for neighbor, weight in self.edges[current_vertex]:
                distance = shortest_paths[current_vertex] + weight

                if distance < shortest_paths[neighbor]:
                    shortest_paths[neighbor] = distance
                    previous_vertices[neighbor] = current_vertex

        path, current_vertex = [], target
        while previous_vertices[current_vertex] is not None:
            path.insert(0, current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.insert(0, start)
        return path if path else None

def parse_input(input_str):
    graph = Graph()
    edges_str, paths_str = input_str.split('/')

    edges_list = edges_str.split(',')
    for edge in edges_list:
        u, weight, v = edge.split()
        graph.add_edge(u, v, int(weight))

    paths_list = paths_str.split(',')
    for path in paths_list:
        start, end = path.split()
        shortest_path = graph.dijkstra(start, end)
        if shortest_path:
            print(f"{start} to {end} : {'->'.join(shortest_path)}")
        else:
            print(f"Not have path : {start} to {end}")


input_str = input("Enter : ")
parse_input(input_str)