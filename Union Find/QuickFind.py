# https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3878/

# UnionFind class
class UnionFind:
    '''
    create an array of size N with the values equal to the corresponding array indices; requires linear time.
    O(N) space complexity
    '''
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x): # O(1)
        return self.root[x]
		
    def union(self, x, y): 
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)): # O(N)
                if self.root[i] == rootY:
                    self.root[i] = rootX

    def connected(self, x, y): # O(1)
        return self.find(x) == self.find(y)


# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true
