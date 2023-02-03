class Solution:
    def dfs(self, node, adj, visit):
        visit[node] = True
        for neighbor in adj[node]:
            if not visit[neighbor]:
                self.dfs(neighbor, adj, visit)

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        adj = [[] for _ in range(n)]
        for connection in connections:
            adj[connection[0]].append(connection[1])
            adj[connection[1]].append(connection[0])

        number_of_connected_components = 0
        visit = [False for _ in range(n)]
        for i in range(n):
            if not visit[i]:
                number_of_connected_components += 1
                self.dfs(i, adj, visit)

        return number_of_connected_components - 1
      
      
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        adj = [list() for _ in range(n)]
        for connection in connections:
            adj[connection[0]].append(connection[1])
            adj[connection[1]].append(connection[0])

        numberOfConnectedComponents = 0
        visit = [False] * n
        for i in range(n):
            if not visit[i]:
                numberOfConnectedComponents += 1
                self.bfs(i, adj, visit)

        return numberOfConnectedComponents - 1

        
    def bfs(self, node, adj, visit):
        q = deque([node])
        visit[node] = True

        while q:
            node = q.popleft()
            for neighbor in adj[node]:
                if not visit[neighbor]:
                    visit[neighbor] = True
                    q.append(neighbor)
                    
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        dsu = UnionFind(n)
        numberOfConnectedComponents = n
        for connection in connections:
            if dsu.find(connection[0]) != dsu.find(connection[1]):
                numberOfConnectedComponents -= 1
                dsu.union_set(connection[0], connection[1])

        return numberOfConnectedComponents - 1


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_set(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1
