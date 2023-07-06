# https://leetcode.com/problems/minimum-size-subarray-sum/
# Sliding Window
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if sum(nums) < target:
            return 0
        i = 0
        s = 0
        res = float('inf')
        for j in range(0, n):
            s += nums[j]
            while s >= target:
                res = min(res, j - i + 1)
                s -= nums[i]
                i += 1

        return res if res != float('inf') else 0

# prefix Sum
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(1, n + 1):
            sums.append(sums[i - 1] + nums[i - 1])
        for i in range(1, n + 1):
            to_find = target + sums[i - 1]
            bound = bisect.bisect_left(sums, to_find)
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))
        return 0 if ans == n + 1 else ans
