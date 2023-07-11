class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.LOG = 0
        while (1 << self.LOG) <= n:
            self.LOG += 1
        self.up = [[0] * self.LOG for _ in range(n)]
        self.depth = [0] * n
        for i in range(n):
            if i != 0:
                self.up[i][0] = parent[i]
            else:
                self.up[i][0] = -1
        for v in range(n):
            if v != 0:
                self.depth[v] = self.depth[parent[v]] + 1
            for j in range(1, self.LOG):
                self.up[v][j] = self.up[self.up[v][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for j in range(self.LOG - 1, -1, -1):
            if k >= (1 << j):
                node = self.up[node][j]
                k -= (1 << j)
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node, k)

# ["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
# [[5,[-1,0,0,1,2]],[3,5],[3,2],[2,2],[0,2],[2,1]]
