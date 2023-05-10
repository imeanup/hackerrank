# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/
# https://leetcode.com/contest/weekly-contest-188/

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        r = [0]
        
        def dfs(u, p):
            s = hasApple[u]
            for v in graph[u]:
                if v == p:
                    continue
                if dfs(v, u):
                    r[0] += 2
                    s = True
            return s
        dfs(0, -1)
        return r[0]
