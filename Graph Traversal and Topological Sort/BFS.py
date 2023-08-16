from collections import deque

graph = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: [5],
    5: []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph[node])

    return result

bfs_result = bfs(graph, 1)
print("BFS:", bfs_result)