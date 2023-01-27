# https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/description/
###########################################################################################
# 1st approach
###########################################################################################
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def merge(self, a, b):
        self.parent[self.find(b)] = self.find(a)

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        path = defaultdict(list)
        union = UnionFind(n+1)
        for x, y in edges:
            union.merge(x, y)
            path[x].append(y)
            path[y].append(x)
        ans = [-1] *(n+1)
        for i in range(1, n+1):
            if ans[i] == -1:
                ans[i] = 0
                q = deque([i])
                while q:
                    p = q.popleft()
                    for newp in path[p]:
                        if ans[newp] == -1:
                            ans[newp] = 1 - ans[p]
                            q.append(newp)
                        elif ans[newp] + ans[p] != 1: return -1
        visited = defaultdict(int)
        for i in range(1, n+1):
            ans[i] = 0
            q = deque([i])
            v = {i}
            cnt = 0
            while q:
                cnt += 1
                for _ in range(len(q)):
                    p = q.popleft()
                    for newp in path[p]:
                        if newp not in v:
                            v.add(newp)
                            q.append(newp)
            visited[union.find(i)] = max(visited[union.find(i)], cnt)
        return sum(visited.values())
        

########################################################################################### 
# 2nd approach
###########################################################################################

class Solution:
    def checkBipartite(self, src, color, adj, components):
        q = []
        q.append(src)
        color[src] = 1

        while len(q) > 0:
            k = len(q)
            while k > 0:
                u = q.pop(0)
                components[u] = src
                for i in range(len(adj[u])):
                    if color[adj[u][i]] == -1:
                        color[adj[u][i]] = 1 - color[u]
                        q.append(adj[u][i])
                    elif color[adj[u][i]] == color[u]:
                        return 0
                k -= 1
        return 1

    def bfs(self, src, adj):
        q = []
        q.append(src)
        color = [-1 for i in range(len(adj))]
        vis = [0 for i in range(len(adj))]
        vis[src] = 1
        level = 0

        while len(q) > 0:
            k = len(q)
            while k > 0:
                u = q.pop(0)
                for i in range(len(adj[u])):
                    if not vis[adj[u][i]]:
                        vis[adj[u][i]] = 1
                        q.append(adj[u][i])
                k -= 1
            level += 1
        return level

    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        color = [-1 for i in range(n)]
        # adj = [[] for i in range(n)]
        adj = defaultdict(list)
        components = [-1 for i in range(n)]

        for i in range(len(edges)):
            adj[edges[i][0]-1].append(edges[i][1]-1)
            adj[edges[i][1]-1].append(edges[i][0]-1)
        print(adj)
        for i in range(n):
            if color[i] == -1:
                res = self.checkBipartite(i, color, adj, components)
                if not res:
                    return -1

        comp = [0 for i in range(n)]

        for i in range(n):
            res = self.bfs(i, adj)
            comp[components[i]] = max(comp[components[i]], res)

        return sum(comp)
      

###########################################################################################

###########################################################################################
class Solution:
    # discussion
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges: 
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
        
        seen = [0]*n
        group = []
        for i in range(n): 
            if not seen[i]: 
                seen[i] = 1
                stack = [i]
                group.append([i])
                while stack: 
                    u = stack.pop()
                    for v in graph[u]: 
                        if not seen[v]: 
                            seen[v] = seen[u] + 1
                            stack.append(v)
                            group[-1].append(v)
                        elif seen[u] & 1 == seen[v] & 1: return -1

        def bfs(x): 
            """Return the levels starting from x."""
            ans = 0
            seen = {x}
            queue = deque([x])
            while queue: 
                ans += 1
                for _ in range(len(queue)): 
                    u = queue.popleft()
                    for v in graph[u]: 
                        if v not in seen: 
                            seen.add(v)
                            queue.append(v)
            return ans 
                            
        ans = 0 
        for g in group: ans += max(bfs(x) for x in g)
        return ans 
