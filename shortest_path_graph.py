import heapq

def dijkstra(graph, start, target):
    # Initialize distances and priority queue
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # (distance, node)
    previous = {node: None for node in graph}  # To reconstruct the path

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the target is reached, break early
        if current_node == target:
            break

        # If the current distance is greater, skip processing
        if current_distance > distances[current_node]:
            continue

        # Relax edges
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # Reconstruct the path
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    return distances[target], path  # Shortest distance and path


# Graph representation: {node: [(neighbor, weight), ...]}
graph = {
'a': [('c', 6), ('d', 9)],
'c': [('a', 6), ('b', 3), ('d', 1), ('e', 13)],
'd': [('a', 9), ('b', 2), ('c', 1), ('e', 9)],
'b': [('c', 3), ('d', 2)],
'e': [('c', 13), ('d', 9)],
}

start = 'a'
target = 'e'

shortest_distance, path = dijkstra(graph, start, target)
print(f"Shortest distance: {shortest_distance}")
print(f"Path: {path}")
