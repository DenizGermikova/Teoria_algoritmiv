import heapq
graph = {
    1: [(3,6),(6,8),(4,7)],
    2: [(3,1),(6,2),(4,3),(7,4)],
    3: [(1,6),(8,7),(2,1)],
    4: [(1,7),(5,9),(2,3)],
    5: [(7,5),(4,9)],
    6: [(2,2),(8,3),(1,8)],
    7: [(8,4),(5,5),(2,4)],
    8: [(3,7),(6,3),(7,4)]
}

def dijkstra(graph, start):
    dist = {v: float('inf') for v in graph}
    pred = {v: None for v in graph}

    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue
        
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                pred[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, pred

def restore_path(pred, start, end):
    path = []
    v = end
    while v is not None:
        path.append(v)
        v = pred[v]
    path.reverse()
    return path if path[0] == start else []


# запуск для вершини 1
start = 1
dist, pred = dijkstra(graph, start)

print("Відстані dist:")
for v in sorted(dist):
    print(v, ":", dist[v])

print("\nПопередники pred:")
for v in sorted(pred):
    print(v, ":", pred[v])

print("\nШляхи від 1:")
for v in sorted(graph):
    if v != 1:
        print(f"1 → {v}: {restore_path(pred,1,v)}, вага = {dist[v]}")
