# https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        for i in range(3, n+1):
            dp[i%3] += dp[(i+1)%3] + dp[(i+2)%3]
        return dp[n%3]
        
        
class Solution:
    memory = {}
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n in [1,2]:
            return 1
        if not self.memory.get(n):
            self.memory[n] = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1) 
        return self.memory[n]     
        
        
class Solution:
    @lru_cache
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return n
        if n < 3:
            return 1
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
