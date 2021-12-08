class Solution:

    def dfs(self, graph, i, j):
        if i < 0 or j < 0 or i >= len(graph) or j >= len(graph[0]):
            return

        if graph[i][j] == "0":
            return

        graph[i][j] = "0"
        self.dfs(graph, i - 1, j)
        self.dfs(graph, i + 1, j)
        self.dfs(graph, i, j - 1)
        self.dfs(graph, i, j + 1)

    def numIslands(self, graph: List[List[str]]) -> int:

        count = 0

        for i in range(len(graph)):
            for j in range(len(graph[0])):
                if graph[i][j] == "1":
                    count += 1
                    self.dfs(graph, i, j)
        return count