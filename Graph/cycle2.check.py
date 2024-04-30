from collections import defaultdict

def isCyclicUtil(v, visited, parent, graph):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            if isCyclicUtil(i, visited, v, graph):
                return True
        elif parent != i:
            return True
    return False

def contains_cycle(vertices, edges):
    graph = defaultdict(list)
    for v, w in edges:
        graph[v].append(w)
        graph[w].append(v)
    visited = [False] * vertices
    for i in range(vertices):
        if not visited[i]:
            if isCyclicUtil(i, visited, -1, graph):
                return True
    return False


vertices = 5
edges = [(1, 0), (1, 2), (2, 0), (0, 3), (3, 4)]

if contains_cycle(vertices, edges):
    print("Graph contains cycle")
else:
    print("Graph doesn't contain cycle")
