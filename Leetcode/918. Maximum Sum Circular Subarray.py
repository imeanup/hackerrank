class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        tot_sum = 0
        max_sum = float('-inf')
        min_sum = float('inf')
        cur_max = float('-inf')
        cur_min = float('inf')
        
        for i in nums:
            cur_max = max(cur_max + i, i)
            max_sum = max(cur_max, max_sum)

            cur_min = min(cur_min + i, i)     
            min_sum = min(cur_min, min_sum)

            tot_sum += i
        if min_sum == tot_sum:
            return max_sum
        return max(max_sum, tot_sum - min_sum)
