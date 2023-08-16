from collections import deque

graph = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: [5],
    5: []
}

def dfs(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return result

dfs_result = dfs(graph, 1)
print("DFS:", dfs_result)