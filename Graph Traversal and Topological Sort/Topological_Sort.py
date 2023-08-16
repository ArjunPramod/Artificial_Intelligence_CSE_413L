from collections import deque

graph = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: [5],
    5: []
}

def topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque(node for node in in_degree if in_degree[node] == 0)
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result

topological_result = topological_sort(graph)
print("Topological Sort:", topological_result)