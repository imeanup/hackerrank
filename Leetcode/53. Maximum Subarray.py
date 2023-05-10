class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm
        max_sum = -float('inf')
        current_sum = 0
        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)
            current_sum = max(current_sum, 0)

        return max_sum
