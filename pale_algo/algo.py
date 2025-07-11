from collections import deque


def dfs(graph, start):
    if not graph:
        return []

    visited = set()
    solution = []

    def _dfs(start):
        visited.add(start)
        solution.append(start)

        for neighbor in graph[start]["neighbors"]:
            if neighbor == []:
                continue

            neighbor_id = neighbor[0]
            if neighbor_id not in visited:
                _dfs(neighbor_id)

    _dfs(start)
    return solution


def bfs(graph, start):
    if not graph or start not in graph:
        return []

    visited = set([start])
    queue = deque([start])
    solution = []

    while queue:
        node = queue.popleft()
        solution.append(node)

        for neighbor in graph[node]["neighbors"]:
            if neighbor == []:
                continue

            neighbor_id = neighbor[0]
            if neighbor_id not in visited:
                visited.add(neighbor_id)
                queue.append(neighbor_id)

    return solution
