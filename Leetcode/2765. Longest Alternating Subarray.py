class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = -1
        for i in range(n):
            j = i
            while j + 1 < n and nums[j + 1] - nums[j] == (-1) ** (j - i):
                j += 1
            max_len = max(max_len, j - i + 1)
        return max_len if max_len > 1 else -1
