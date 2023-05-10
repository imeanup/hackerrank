class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = DisjointSet(n)
        for u, v in edges:
            uf.union(u, v)

        graph = {}
        for i in range(n):
            root = uf.find(i)
            if root not in graph:
                graph[root] = 0
            graph[root] += 1

        path = 0
        nodesRem = n
        for e in graph.values():
            graph = e
            path += graph * (nodesRem - e)
            nodesRem -= graph
        return path

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                px, py = py, px
            self.parent[px] = py
            if self.rank[px] == self.rank[py]:
                self.rank[py] += 1

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)
    
