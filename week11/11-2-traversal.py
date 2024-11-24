data = input("Enter : ").split(",")
graph = {}
for i in data :
    a, b = i.split(" ")
    if a not in graph: graph.update({a: []})
    if b not in graph: graph.update({b: []})

    graph[a].append(b)
    graph[b].append(a)

v = [i for i in graph.keys()]

def bfs(graph, start, visited):
    queue = [start]
    visited.add(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbor in sorted(graph[node]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node, end=' ')

    for neighbor in sorted(graph[node]):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def dfs_disconnected(graph):
    visited = set()
    for node in sorted(graph.keys()):
        if node not in visited:
            dfs(graph, node, visited)

def bfs_disconnected(graph):
    visited = set()
    for node in sorted(graph.keys()):
        if node not in visited:
            bfs(graph, node, visited)


print("Depth First Traversals : ", end="")
dfs_disconnected(graph)
print()
print("Bredth First Traversals : ", end="")
bfs_disconnected(graph)
