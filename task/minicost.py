import heapq

def findCheapestPrice(n, flights, src, dst):
    # Create adjacency list from flights
    graph = {i: [] for i in range(n)}
    for u, v, w in flights:
        if u not in graph:
            graph[u] = []
        graph[u].append((v, w))

    # Dijkstra's algorithm
    min_costs = [float('inf')] * n
    min_costs[src] = 0
    pq = [(0, src)]

    while pq:
        cost, node = heapq.heappop(pq)
        if node == dst:
            return cost
        if cost > min_costs[node]:
            continue
        for neighbor, w in graph.get(node, []):
            if cost + w < min_costs[neighbor]:
                min_costs[neighbor] = cost + w
                heapq.heappush(pq, (cost + w, neighbor))

    return -1

# Example usage:
if __name__ == "__main__":
    n1 = 4
    flights1 = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src1 = 0
    dst1 = 3
    print("Output:", findCheapestPrice(n1, flights1, src1, dst1))  # Output: 400

    n2 = 4
    flights2 = [[1,0,200],[0,3,100],[0,2,50],[0,4,500],[2,1,100],[2,4,50],[4,1,600]]
    src2 = 0
    dst2 = 4
    print("Output:", findCheapestPrice(n2, flights2, src2, dst2))  # Output: 100
