from scripts.leet75.dfs import dfs, bfs, create_graph

"""test_cases = [create_graph(),['A', 'B', 'D', 'F', 'E', 'C']]"""

class Test:
    test_cases = [
        ['A', 'B', 'D', 'E', 'F', 'C'],
        ['A', 'B', 'C', 'D', 'E', 'F'],
    ]
    testable_functions = []

    def test_create_graph(self):
        graph = create_graph()
        verticies = ["A", "B", "C", "D", "E", "F"]
        for letter in verticies:
            assert letter in graph

    def test_dfs(self):
        graph = create_graph()
        assert dfs(graph, "A") == self.test_cases[0]
    
    def test_bfs(self):
        graph = create_graph()
        assert bfs(graph, "A") == self.test_cases[1]