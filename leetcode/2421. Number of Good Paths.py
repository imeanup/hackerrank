# # Approach 1: DFS (TLE)
# from collections import defaultdict, Counter

# class Solution:
#     def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
#         if len(vals) == 1:
#             return 1

#         graph = defaultdict(list)

#         for u, v in edges:
#             graph[u].append(v)
#             graph[v].append(u)
        
#         cnt = Counter(vals)
#         n = len(vals)
#         ans = 0

#         # print(cnt)
        
#         def dfs(source):
#             # print(source)
#             # print(vals)
#             if cnt[vals[source]] == 1:
#                 return 0
            
#             r = 0

#             stack = [source]
#             visited = {source}

#             while stack:
#                 node = stack.pop()

#                 for e in graph[node]:
#                     if vals[e] > vals[source]:
#                         continue
#                     if e not in visited:
#                         if e > source and vals[e] == vals[source]:
#                             r += 1
#                         visited.add(e)
#                         stack.append(e)
            
#             return r

#         for i in range(n):
#             ans += dfs(i)
        
#         return ans + len(vals)

# # Approach 2: DSU
# from collections import Counter, defaultdict
# from itertools import combinations

# class QuickUnion:
#     def __init__(self, n) -> None:
#         self.parents = list(range(n))
    
#     def find(self, p):
#         while p != self.parents[p]:
#             p = self.parents[p]
#         return p
    
#     def union(self, p, q):
#         rp, rq = self.find(p), self.find(q)

#         if rp != rq:
#             self.parents[rq] = rp
    
#     def connected(self, p, q):
#         return self.find(p) == self.find(q)


# class Solution:
#     def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
#         n = len(vals)

#         if n == 1:
#             return 1

#         # cnt = Counter(vals)
#         dsu = QuickUnion(n)
        
#         # build val map
#         val_map = defaultdict(list)
#         for i, v in enumerate(vals):
#             val_map[v].append(i)
#         cand_vals = sorted(val_map.keys())

#         ans = n

#         # print(cand_vals)
#         for val in cand_vals:
#             # union
#             for u, v in edges:
#                 if vals[u] <= val and vals[v] <= val:
#                     dsu.union(u, v)
            
#             # check
#             if len(val_map[val]) == 1:
#                 continue
            
#             # for i in range(n):
#             #     for j in range(i+1, n):
#             #         if vals[i] == vals[j] == val and dsu.connected(i, j):
#             #             ans += 1

#             for u, v in combinations(val_map[val], 2):
#                 if dsu.connected(u, v):
#                     ans += 1

#         return ans


# # Approach 3: Advanced DSU
# # https://leetcode.com/problems/number-of-good-paths/solutions/2620680/python-union-find-solution/
# class Solution:
#     def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
#         ans = n = len(vals)
#         E = sorted([(max(vals[u], vals[v]), u, v) for u, v in edges])
#         parents = list(range(n))
#         count = [{vals[i]: 1} for i in range(n)]

#         def find(p):
#             while p != parents[p]:
#                 p = parents[p]
#             return p

#         for w, i, j in E:
#             ri, rj = find(i), find(j)  # find
#             ci, cj = count[ri].get(w, 0), count[rj].get(w, 0)  # count
#             count[ri] = {w:ci+cj}  # update subtree root count
#             ans += ci*cj
#             parents[rj] = ri  # union

#         return ans


# Approach 4: Optimized Advanced DSU
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        ans = n = len(vals)
        edges.sort(key=lambda x: max(vals[x[0]], vals[x[1]]))
        # print(edges)
        parents = list(range(n))
        count = [1] * n

        # def find(p):
        #     while p != parents[p]:
        #         p = parents[p]
        #     return p
        def find(p):
            if p != parents[p]:
                parents[p] = find(parents[p])
            return parents[p]

        for i, j in edges:
            ri, rj = find(i), find(j)  # find
            ci, cj = count[ri], count[rj]  # count
            vi, vj = vals[ri], vals[rj]  # max value of subtree
            if vi == vj:
                count[ri] += cj  # update subtree root count
                parents[rj] = ri  # union
                ans += ci * cj
            elif vi < vj:
                parents[ri] = rj
            else:
                parents[rj] = ri

        return ans

# class Solution:
#     def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
#         '''
#         node ---> DFS ---> find smae node vals
#         children will child.val <= start.val
                
        
#         '''
#         edges.sort(key=lambda x: max(vals[x[0]], vals[x[1]]))
#         n = len(vals)
#         parent = list(range(n))
#         count= [1]*n


#         def find(i):
#             if parent[i] != i:
#                 parent[i] = find(parent[i])
#             return parent[i]
#         res = 0


#         for i, j in edges:
#             parentI, parentJ = find(i), find(j)
#             if vals[parentI] == vals[parentJ]:
#                 parent[parentJ] = parentI
#                 res += count[parentJ] * count[parentI]
#                 count[parentI] += count[parentJ]
#             elif vals[parentI] < vals[parentJ]:
#                 parent[parentI] = parentJ
#             else:
#                 parent[parentJ] = parentI

#         return res + n
