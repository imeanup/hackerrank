# https://leetcode.com/problems/where-will-the-ball-fall/description/
# https://leetcode.com/contest/weekly-contest-221

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = len(grid[0])
        dp = [i for i in range(m)]
        for i in range(n-1, -1, -1):
            ndp = [-1]*m
            for j in range(m):
                if grid[i][j] == -1:
                    if j-1>=0 and grid[i][j-1]==-1:
                        ndp[j] = dp[j-1]
                else:
                    if j+1 < m and grid[i][j+1] == 1:
                        ndp[j] = dp[j+1]
            dp = ndp
        return dp
        
