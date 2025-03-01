import heapq
import timeit

def dijkstra(graph, start, end):
    queue = [(0, start)]
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
    
    return distances, previous_nodes

def find_path(previous_nodes, start, end):
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.reverse()
    return path if path[0] == start else None

def main():
    graph = {
        'A': [('B', 22), ('C', 9), ('D', 12)],
        'B': [('A', 22), ('C', 35), ('F', 36), ('H', 34)],
        'C': [('A', 9), ('B', 35), ('D', 4), ('E', 65), ('F', 42)],
        'D': [('A', 12), ('C', 4), ('E', 33), ('I', 30)],
        'E': [('C', 65), ('D', 33), ('F', 18), ('G', 23)],
        'F': [('B', 36), ('C', 42), ('E', 18), ('G', 39), ('H', 24)],
        'G': [('E', 23), ('F', 39), ('H', 25), ('I', 21)],
        'H': [('B', 34), ('F', 24), ('G', 25), ('I', 19)],
        'I': [('D', 30), ('G', 21), ('H', 19)]
    }
    distances, previous_nodes = dijkstra(graph, 'A', 'I')
    shortest_path = find_path(previous_nodes, 'A', 'I')
    
    print(f"Shortest path from A to I using Dijkstra's Algorithm: {shortest_path}")
    print(f"Distance: {distances['I']}")

if __name__ == "__main__":
    time_taken = timeit.timeit(main, number=1)
    print(f"Time taken: {time_taken:.10f} seconds")