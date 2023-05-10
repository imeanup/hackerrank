# https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind(len(nums))
        valToIndex = {}
        for i in range(len(nums)):
            if nums[i] in valToIndex:
                continue
            if nums[i] - 1 in valToIndex:
                uf.union(i, valToIndex[nums[i] - 1])
            if nums[i] + 1 in valToIndex:
                uf.union(i, valToIndex[nums[i] + 1])
            valToIndex[nums[i]] = i
        
        return uf.getLargestComponentSize()

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
    
    def union(self, x, y): 
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def getLargestComponentSize(self):
        maxSize = 0
        for i in range(len(self.parent)):
            if self.parent[i] == i and self.size[i] > maxSize:
                maxSize = self.size[i]
        return maxSize
