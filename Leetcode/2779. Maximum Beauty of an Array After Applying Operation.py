class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_beauty = 1
        i = 0
        for j in range(1, len(nums)):
            while nums[j] - nums[i] > 2 * k:
                i += 1
            max_beauty = max(max_beauty, j - i + 1)
        return max_beauty
