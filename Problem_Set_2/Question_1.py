def solve(n, m, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [0] * (n + 1)
    directions = {}
    set_A = set()
    set_B = set()

    def dfs(node, current_set):
        visited[node] = current_set
        if current_set == 1:
            set_A.add(node)
        else:
            set_B.add(node)

        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                if not dfs(neighbor, 3 - current_set): 
                    return False
            elif visited[neighbor] == current_set:
                return False
        return True

    if not dfs(1, 1):
        return -1

    for u, v in edges:
        if visited[u] == 1 and visited[v] == 2:
            directions[(u, v)] = 0
            directions[(v, u)] = 1
        else:
            directions[(u, v)] = 1
            directions[(v, u)] = 0

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
