# https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/description/
# https://leetcode.com/contest/weekly-contest-328/problems/difference-between-maximum-and-minimum-price-sum/

class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        tree = [[] for _ in range(n)]
        for u, v in edges: 
            tree[u].append(v)
            tree[v].append(u)
        
        def dfs(u, p):
            nonlocal ans
            include = [] # include leaf value 
            exclude = [] # exclude leaf value
            for v in tree[u]: 
                if v != p: 
                    x, y = dfs(v, u)
                    include.append((x+price[u], v))
                    exclude.append((y+price[u], v))
            if not include: 
                include = [(price[u], u)]
                exclude = [(0, u)]
            if len(include) == 1: ans = max(ans, include[0][0] - price[u], exclude[0][0])
            else: 
                include.sort(reverse=True)
                for e, v in exclude: 
                    if v != include[0][1]: cand = e + include[0][0] - price[u]
                    else: cand = e + include[1][0] - price[u]
                    ans = max(ans, cand)
            return include[0][0], max(exclude)[0]
        
        ans = 0 
        dfs(0, -1)
        return ans 
      
class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        adj = collections.defaultdict(set)
        
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        @cache
        def dfs(node, parent):
            curr_price = price[node]
            m = 0
            for v in adj[node]:
                if v == parent:
                    continue
                m = max(m, dfs(v, node))
            return curr_price + m
        
        m = 0
        for node in range(n):
            max_price = dfs(node, -1)
            min_price = price[node]
            m = max(m, max_price-min_price)

        return m
