# https://leetcode.com/problems/smallest-string-with-swaps/description/

from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n # We don't need any size here.
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.size[px] > self.size[py]:
                px, py = py, px
            self.parent[px] = py
            self.size[py] += self.size[px]

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)
        for i, j in pairs:
            uf.union(i, j)
        d = {}
        for i in range(n):
            p = uf.find(i)
            if p not in d:
                d[p] = []
            d[p].append(i)
        res = [''] * n
        for _, nodes in d.items():
            nodes.sort()
            for i, j in zip(nodes, sorted(s[i] for i in nodes)):
                res[i] = j
        return ''.join(res)
      
# https://leetcode.com/problems/smallest-string-with-swaps/submissions/880505216/
'''
s = "dcab"; pairs = [[0,3],[1,2]] #"bacd"
# s = "dcab"; pairs = [[0,3],[1,2],[0,2]] #"abcd"
# s = "cba"; pairs = [[0,1],[1,2]]
c = Solution()
print(c.smallestStringWithSwaps(s, pairs))
'''
