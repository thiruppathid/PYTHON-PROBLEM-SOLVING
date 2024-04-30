d = {}
visited=set()
def add_edge(node, edge):
    if node in d:
        d[node].append(edge)
    else:
        d[node] = [edge]

    if edge in d:
        d[edge].append(node)
    else:
        d[edge] = [node]

def bfs(start_node):
    queue = []
    #visited = set()
    queue.append(start_node)
    visited.add(start_node)
    while queue:
        cur = queue.pop(0)
        print(cur, end=" ")
        for neighbour in d.get(cur, []):
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)

# Input processing
for _ in range(int(input())):
    node, edge = map(int, input().split())
    add_edge(node, edge)
c=0
# Check if all nodes are connected
print(d)
for key, ele in d.items():
    if key in visited:
        c=1
        continue
    else:
        print("Disconnected")
        c=0
        break
if(c==1):
    print("Connected")
