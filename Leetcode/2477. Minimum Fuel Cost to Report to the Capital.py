class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        adj = [[] for _ in range(n)]
        for road in roads:
            adj[road[0]].append(road[1])
            adj[road[1]].append(road[0])

        self.fuel = 0

        def dfs(node, parent, adj, seats):
            representatives = 1
            for child in adj[node]:
                if child != parent:
                    representatives += dfs(child, node, adj, seats)
            if node != 0:
                self.fuel += math.ceil(representatives / seats)
            return representatives

        dfs(0, -1, adj, seats)
        return self.fuel
      
      
from math import ceil
from collections import deque

class Solution:
    def bfs(self, n, adj, degree, seats):
        q = deque()
        for i in range(1, n):
            if degree[i] == 1:
                q.append(i)

        representatives = [1] * n
        fuel = 0

        while q:
            node = q.popleft()
            fuel += ceil(representatives[node] / seats)
            for neighbor in adj[node]:
                degree[neighbor] -= 1
                representatives[neighbor] += representatives[node]
                if degree[neighbor] == 1 and neighbor != 0:
                    q.append(neighbor)

        return fuel

    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        adj = [[] for _ in range(n)]
        degree = [0] * n

        for road in roads:
            adj[road[0]].append(road[1])
            adj[road[1]].append(road[0])
            degree[road[0]] += 1
            degree[road[1]] += 1

        return self.bfs(n, adj, degree, seats)
