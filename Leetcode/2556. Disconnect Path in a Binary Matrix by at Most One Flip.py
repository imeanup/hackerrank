# https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/

class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        a = [[0 for j in range(m)] for i in range(n)]
        b = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                a[i][j] = grid[i][j] and (not i and not j or i and a[i-1][j] or j and a[i][j-1])
        if not a[n-1][m-1]:
            return True
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                b[i][j] = grid[i][j] and (i == n-1 and j == m-1 or i != n-1 and b[i+1][j] or j != m-1 and b[i][j+1])
        d = [0 for i in range(n + m - 1)]
        for i in range(n):
            for j in range(m):
                if a[i][j] and b[i][j]:
                    d[i+j] += 1
        for i in range(1, n + m - 2):
            if d[i] == 1:
                return True
        return False
