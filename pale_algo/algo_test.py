# This a unit test for our algorithms from algo module. We decided that
# TDD (Test Driven Development) is the best approach to develop algorithms, we know how DFS, BFS,
# A-Star... work and what they emit as solutions, but not implement as
# code, so we write test cases and their solution and compare it to
# what the code emits.

import unittest

import algo

# test cases are graphs with JSON structure (because we must send them
# over the network), so their schema must be unified.
# Graph schema will look like this:
#
# graph
#   - node_id:
#       - name: "name"
#       - neighbors: [
#           (id0, cost or NULL, heuristic or NULL),
#           (id1, cost or NULL, heuristic or NULL),
#           ...
#       ]
#   - id0:
#       - name: "name0"
#       - neighbors: [(node_id, cost or NULL, heuristic or NULL), ...]
#   ...

# Test cases
# Graphs like trees:
graph0 = {
    0: {"name": "A", "neighbors": [(1, 1, 1), (2, 3, 2)]},
    1: {"name": "B", "neighbors": [(3, 1, 1), (4, 2, 1), (5, 4, 3)]},
    2: {"name": "C", "neighbors": [(6, 8, 2), (7, 18, 14)]},
    3: {"name": "D", "neighbors": []},
    4: {"name": "E", "neighbors": []},
    5: {"name": "F", "neighbors": [(8, 12, 11)]},
    6: {"name": "H", "neighbors": []},
    7: {"name": "I", "neighbors": []},
    8: {"name": "V", "neighbors": []},
}

graph1 = {
    0: {"name": "A", "neighbors": [(1,), (2,)]},
    1: {"name": "B", "neighbors": [(3,), (4,), (5,)]},
    2: {"name": "C", "neighbors": [(6,), (7,)]},
    3: {"name": "D", "neighbors": []},
    4: {"name": "E", "neighbors": []},
    5: {"name": "F", "neighbors": [(8,)]},
    6: {"name": "H", "neighbors": []},
    7: {"name": "I", "neighbors": []},
    8: {"name": "V", "neighbors": []},
}

# Cycle Graphs:
cycle_graph = {
    0: {"name": "A", "neighbors": [(1, 1, 1), (2, 3, 2)]},
    1: {"name": "B", "neighbors": [(3, 1, 1), (4, 2, 1), (5, 4, 3)]},
    2: {"name": "C", "neighbors": [(6, 8, 2), (7, 18, 14)]},
    3: {"name": "D", "neighbors": []},
    4: {"name": "E", "neighbors": []},
    5: {"name": "F", "neighbors": [(8, 12, 11)]},
    6: {"name": "H", "neighbors": []},
    7: {"name": "I", "neighbors": []},
    8: {"name": "V", "neighbors": [(0, 20, 18)]},
}

# One Node Graphs:
one_node_graph = {17: {"name": "Pale", "neighbors": []}}

# Empty Graphs:
empty_graph = {}

# Disconnected Graph
disconnected_graph = {
    0: {"name": "A", "neighbors": [(1, 1, 1), (2, 3, 2)]},
    1: {"name": "B", "neighbors": [(3, 1, 1), (4, 2, 1)]},
    2: {"name": "C", "neighbors": [(6, 8, 2), (7, 18, 14)]},
    3: {"name": "D", "neighbors": []},
    4: {"name": "E", "neighbors": []},
    5: {"name": "F", "neighbors": [(8, 12, 11)]},
    6: {"name": "H", "neighbors": []},
    7: {"name": "I", "neighbors": []},
    8: {"name": "V", "neighbors": [(0, 20, 18)]},
}

# Graphs with Invalid ID:
invalid_graph = {
    0: {"name": "A", "neighbors": [(1, 1, 1), (2, 3, 2)]},
    1: {"name": "B", "neighbors": [(3, 1, 1), (4, 2, 1), (5, 3, 2)]},
    2: {"name": "C", "neighbors": [(6, 8, 2), (7, 18, 14)]},
    3: {"name": "D", "neighbors": []},
    4: {"name": "E", "neighbors": []},
    5: {"name": "F", "neighbors": [(500, 12, 11)]},
    6: {"name": "H", "neighbors": []},
    7: {"name": "I", "neighbors": []},
    8: {"name": "V", "neighbors": [(0, 20, 18)]},
}


class DFSTest(unittest.TestCase):
    def test_trees(self):
        self.assertListEqual(algo.dfs(graph0, 0), [0, 1, 3, 4, 5, 8, 2, 6, 7])
        self.assertListEqual(algo.dfs(graph1, 0), [0, 1, 3, 4, 5, 8, 2, 6, 7])

    def test_cycle_graph(self):
        self.assertListEqual(algo.dfs(cycle_graph, 0), [0, 1, 3, 4, 5, 8, 2, 6, 7])

    def test_one_node_graph(self):
        self.assertListEqual(algo.dfs(one_node_graph, 17), [17])

    def test_empty_graph(self):
        self.assertListEqual(algo.dfs(empty_graph, 0), [])

    def test_disconnected_graph(self):
        self.assertListEqual(algo.dfs(disconnected_graph, 0), [0, 1, 3, 4, 2, 6, 7])

    def test_invalid_graph(self):
        self.assertRaises(KeyError, algo.dfs, invalid_graph, 0)


class BFSTest(unittest.TestCase):
    def test_trees(self):
        self.assertListEqual(algo.bfs(graph0, 0), [0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.assertListEqual(algo.bfs(graph1, 0), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_cycle_graph(self):
        self.assertListEqual(algo.bfs(cycle_graph, 0), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_one_node_graph(self):
        self.assertListEqual(algo.bfs(one_node_graph, 17), [17])

    def test_empty_graph(self):
        self.assertListEqual(algo.bfs(empty_graph, 0), [])

    def test_disconnected_graph(self):
        self.assertListEqual(algo.bfs(disconnected_graph, 0), [0, 1, 2, 3, 4, 6, 7])

    def test_invalid_graph(self):
        self.assertRaises(KeyError, algo.bfs, invalid_graph, 0)


if __name__ == "__main__":
    unittest.main()
