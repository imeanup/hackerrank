class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        memo = {}
        cuts = [0] + sorted(cuts) + [n]
        
        def cost(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if right - left == 1:
                return 0
            ans = min(cost(left, mid) + cost(mid, right) + cuts[right] - cuts[left] for mid in range(left + 1, right))
            memo[(left, right)] = ans
            return ans
        
        return cost(0, len(cuts) - 1)

    
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        m = len(cuts)
        cuts = [0] + sorted(cuts) + [n]
        
        dp = [[0] * (m + 2) for _ in range(m + 2)]
        
        for diff in range(2, m + 2):
            for left in range(m + 2 - diff):
                right = left + diff
                ans = float('inf')
                for mid in range(left + 1, right):
                    ans = min(ans, dp[left][mid] + dp[mid][right] + cuts[right] - cuts[left])
                dp[left][right] = ans
        
        return dp[0][m + 1]

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]
        m = len(cuts)
        dp = [[float('inf')] * m for _ in range(m)]
        for i in range(m - 1):
            dp[i][i + 1] = 0
        for L in range(2, m):
            for i in range(m - L):
                j = i + L
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
                dp[i][j] += cuts[j] - cuts[i]
        return dp[0][m - 1]
