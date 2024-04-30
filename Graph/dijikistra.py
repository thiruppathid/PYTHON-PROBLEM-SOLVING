import heapq

def dijkstra(adj,src,des,n):
    shortest={}
    minheap=[[src,0]]
    while minheap:
        n1,w1=heapq.heappop(minheap)
        if n1 not in shortest:
            shortest[n1]=w1 
        else:
            continue
        for n2,w2 in adj[n1]:
            heapq.heappush(minheap,[n2,w1+w2])
    

    for i in range(n):
        if i not in shortest:
            shortest[i]=-1

    return shortest[des]

n=4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src=2
des=3
adj={}
for i in range(n):
        adj[i]=[]
for s,d,weight in flights:
        adj[s].append([d,weight])


print(dijkstra(adj,src,des,n))