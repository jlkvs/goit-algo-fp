import heapq
def add_edge(graph, u, v, weight):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, weight))
    graph[v].append((u, weight))  

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    min_heap = [(0, start)]  
    heapq.heapify(min_heap)
    
    while min_heap:
        current_distance, u = heapq.heappop(min_heap)
        
        if current_distance > distances[u]:
            continue
        
        for v, weight in graph[u]:
            distance = current_distance + weight
            
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(min_heap, (distance, v))
    
    return distances

graph = {}
add_edge(graph, 'A', 'B', 1)
add_edge(graph, 'A', 'C', 4)
add_edge(graph, 'B', 'C', 2)
add_edge(graph, 'B', 'D', 5)
add_edge(graph, 'C', 'D', 1)
add_edge(graph, 'D', 'E', 3)

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)

print(f"Найкоротші відстані від вершини {start_vertex}:")
for vertex, distance in distances.items():
    print(f"Відстань до {vertex}: {distance}")
