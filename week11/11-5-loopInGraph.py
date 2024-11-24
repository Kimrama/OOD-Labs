
def build_graph(edges):
    graph = {}
    for edge in edges:
        u, v = edge.split()  
        u, v = int(u), int(v)
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
    return graph


def is_cycle_in_graph(graph, num_nodes):
    visited = [0] * num_nodes  

    def dfs(node):
        if visited[node] == 1:  
            return True
        if visited[node] == 2:  
            return False
        
        visited[node] = 1 
        
        if node in graph:  
            for neighbor in graph[node]:  
                if dfs(neighbor):  
                    return True
        
        visited[node] = 2 
        return False

    for node in range(num_nodes): 
        if visited[node] == 0:  
            if dfs(node):  
                return True
    return False  


def check_cycle():
    edges_input = input("Enter : ")  
    edges = edges_input.split(',')
    all_nodes = set() 
    
    for edge in edges:
        u, v = edge.split()
        all_nodes.add(int(u))
        all_nodes.add(int(v))
    
    num_nodes = len(all_nodes) 
    graph = build_graph(edges) 
    
    if is_cycle_in_graph(graph, num_nodes):
        print("Graph has a cycle")
    else:
        print("Graph has no cycle")


check_cycle()
