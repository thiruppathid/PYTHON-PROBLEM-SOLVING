d={}
def addedge(node,vertex):
    if node in d:
        d[node].append(vertex)
    else:
        d[node]=[vertex]
    if vertex in d:
        d[vertex].append(node)
    else:
        d[vertex]=[node]
def bfs(cur):
    queue=[cur]
    visited=set()
    visited.add(cur)
    while queue:
        cur=queue.pop(0)
        print(cur,end=" ")
        for neighbour in d[cur]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
                
        
for _ in range(int(input())):
    u,v=map(int,input().split())
    addedge(u,v)
bfs(0)