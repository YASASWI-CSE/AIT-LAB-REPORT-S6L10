def dfs(graph, start):
    stack, visited = [start], set()
    print("DFS:", end=" ")
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # Add unvisited neighbors in reverse order to maintain traversal order
            stack.extend(reversed([neighbor for neighbor in graph[node] if neighbor not in visited]))
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

dfs(graph, 'P')
