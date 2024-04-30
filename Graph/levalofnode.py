from collections import defaultdict, deque

def add_edge(adj_list, u, v):
    adj_list[u].append(v)
    adj_list[v].append(u)

def find_level(adj_list, start, target):
    visited = set()
    level = defaultdict(int)
    queue = deque([(start, 0)])

    while queue:
        node, curr_level = queue.popleft()
        if node == target:
            return curr_level
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                queue.append((neighbor, curr_level + 1))
                visited.add(neighbor)
                level[neighbor] = curr_level + 1

    return -1  # If target not found

# Example usage:
if __name__ == "__main__":
    V = 3  # Number of vertices
    adj_list = defaultdict(list)

    # Adding edges to the graph
    add_edge(adj_list, 0, 1)
    add_edge(adj_list, 0, 2)
    add_edge(adj_list, 1, 3)
    add_edge(adj_list, 1, 4)

    node_X = 3  # Node to find the level of
    level = find_level(adj_list, 0, node_X)

    if level != -1:
        print(f"The level of node {node_X} is {level}.")
    else:
        print(f"Node {node_X} does not exist in the graph.")
