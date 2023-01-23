# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = DisjointSet(n+1)
        ans = sys.maxsize
        for road in roads:
            uf.union(road[0], road[1])

        for road in roads:
            if uf.find(1) == uf.find(road[0]):
                ans = min(ans, road[2])

        return ans

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
