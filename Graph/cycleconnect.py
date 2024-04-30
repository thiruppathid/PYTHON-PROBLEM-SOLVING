def is_cyclic(vertices, edges):
    graph = [[] for _ in range(vertices)]

    # Build the adjacency list representation of the graph
    for u, v in edges:
        graph[u].append(v)

    def is_cyclic_util(v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True

        for neighbor in graph[v]:
            if not visited[neighbor]:
                if is_cyclic_util(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[v] = False
        return False

    visited = [False] * vertices
    rec_stack = [False] * vertices

    for vertex in range(vertices):
        if not visited[vertex]:
            if is_cyclic_util(vertex, visited, rec_stack):
                return True
    return False

# Example usage:
vertices = 4
edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]

if is_cyclic(vertices, edges):
    print("Graph contains a cycle")
else:
    print("Graph does not contain a cycle")
