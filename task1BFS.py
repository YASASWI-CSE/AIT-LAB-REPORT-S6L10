from collections import deque  # ✅ You need this import for deque

def bfs(graph, start):
    queue, visited = deque([start]), set()   # Initialize queue and visited set
    print("BFS:", end=" ")
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # Add unvisited neighbors to the queue
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
    print()

# Example graph
graph = {
    'P': ['Q', 'R'],
    'Q': ['P', 'S', 'T'],
    'R': ['P', 'U'],
    'S': ['Q'],
    'T': ['Q', 'U'],
    'U': ['R', 'T']
}

bfs(graph, 'P')
