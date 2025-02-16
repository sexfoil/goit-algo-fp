import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.vertices:
            self.vertices[from_vertex] = []
        if to_vertex not in self.vertices:
            self.vertices[to_vertex] = []
        self.vertices[from_vertex].append((to_vertex, weight))


def dijkstra(graph, start_vertex):
    distances = {vertex: float('infinity') for vertex in graph.vertices.keys()}
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.vertices.get(current_vertex, []):
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'C', 1)
    graph.add_edge('B', 'D', 2)
    graph.add_edge('C', 'D', 1)

    print("Ребра графа:")
    for vertex, edges in graph.vertices.items():
        print(f"{vertex}: {edges}")

    distances = dijkstra(graph, 'A')
    print("\nНайкоротший шлях з вершини 'A':")
    for vertex, distance in distances.items():
        print(f"{vertex}: {distance}")

