from collections import defaultdict
add_list=defaultdict(list)


def bfs(start,add_list):
    visited=set()
    que=[start]
    visited.add(start)
    while que:
        cur=que.pop(0)
        for neighbour in add_list[cur]:
            if neighbour in visited:
                print("yes")
                return
            else:
                que.append(neighbour)
                visited.add(neighbour)
    print("No")
def dfs(start,add_list):    
    visited = set()
    que = [start]
    visited.add(start)
    try:
        while que:
            cur = que.pop()
            for neighbour in add_list[cur]:
                if neighbour in visited:
                    print("Loop Occurred")
                    exit(0)
                    return 
                else:
                    que.append(neighbour)
                    visited.add(neighbour)
    except:
        raise("no way")
    print("No loop occurred")

n = int(input("Enter the number of edges: "))
for _ in range(n):
    node, edge = map(int, input().split())
    #add_edge(node, edge)
    add_list[node].append(edge)
print("Graph representation:")
print(add_list)
bfs(0,add_list)

