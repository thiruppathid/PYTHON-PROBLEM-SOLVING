d = {}
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
    visited = set()
    #val=[]
    queue.append(start_node)
    visited.add(start_node)
    while queue:
        cur=queue.pop()
        #val.append(cur)
        print(cur,end=" ")
        for neighbour in (d.get(cur,[])):
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
def dfs(start_node):
    stack=[]
    visited=set()
    stack.append(start_node)
    visited.add(start_node)
    while stack:
        cur=stack.pop()
        print(cur,end=" ")
        for neighbour in (d.get(cur,[])):
            if neighbour not in visited:
                stack.append(neighbour)
                visited.add(neighbour)
            


    #print(val)
n = int(input("Enter how many connections: "))
for _ in range(n):
    n, v = map(int, input("Enter node and edge: ").split())
    add_edge(n, v)

for u, v in d.items():
    print(u, "->", *v)

start_node = 0
bfs(start_node)
print()
dfs(3)
