def dfs(graph, start):
    visited = set()
    solution = []

    if not graph:
        return []

    def _dfs(start):
        visited.add(start)
        solution.append(start)

        for neighbor in graph[start]["neighbors"]:
            if neighbor == []:
                continue

            if neighbor[0] not in visited:
                _dfs(neighbor[0])

    _dfs(start)
    return solution
