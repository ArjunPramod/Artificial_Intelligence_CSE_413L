def dfs(node, graph, visited, directions):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            directions[(node, neighbor)] = 0
            directions[(neighbor, node)] = 1
            dfs(neighbor, graph, visited, directions)

def solve(n, m, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    directions = {}
    
    dfs(1, graph, visited, directions)
    
    for node in range(1, n + 1):
        indegree = sum(directions.get((u, node), 0) for u in graph[node])
        if indegree % 2 != 0:
            return -1
    
    result = [directions.get(edge, 0) for edge in edges]
    return result

t = 1  
test_cases = [
    (4, 4, [(1, 2), (1, 3), (2, 4), (3, 4)]),
    (3, 3, [(1, 2), (2, 3), (1, 3)])
]

for n, m, edges in test_cases:
    result = solve(n, m, edges)
    if result == -1:
        print(-1)
    else:
        print(" ".join(map(str, result)))