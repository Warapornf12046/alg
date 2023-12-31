import heapq

def dijkstra(graph, start):
    # Initialize distances and predecessors
    distances = {vertex: float('infinity') for vertex in graph}
    predecessors = {vertex: None for vertex in graph}
    distances[start] = 0
    
    # Priority queue to keep track of vertices with their distances
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Get the vertex with the smallest distance from the priority queue
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # If current distance is greater than the recorded distance, skip
        if current_distance > distances[current_vertex]:
            continue
        
        # Explore neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # If the new distance is shorter, update distance and predecessor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, predecessors

# Example usage
if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    
    start_vertex = 'A'
    distances, predecessors = dijkstra(graph, start_vertex)
    
    print("Shortest distances from", start_vertex)
    for vertex, distance in distances.items():
        print(f"To {vertex}: {distance}")