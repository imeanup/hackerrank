# https://leetcode.com/problems/number-of-great-partitions/description/

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        if sum(nums) < 2 * k:
            return 0
        
        n = len(nums)
        
        MOD = 10 ** 9 + 7
        
        tot = pow(2, n, MOD)
        
        low = [1] + [0] * (k - 1)
        
        for v in nums:
            nl = low[:]
            
            for i in range(k - v):
                low[i + v] += nl[i]
                low[i + v] %= MOD
                
        tot -= 2 * sum(low)
        return tot % MOD
