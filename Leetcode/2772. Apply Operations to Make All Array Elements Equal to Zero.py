class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        diff[0] = nums[0]
        for i in range(1, n):
            diff[i] = nums[i] - nums[i - 1]
        for i in range(n):
            if diff[i] < 0:
                return False
            if diff[i] and i + k <= n:
                diff[i + k] += diff[i]
                diff[i] = 0
        for i in range(n):
            if diff[i]:
                return False
        return True

  # Solution from 	py-is-best-lang in the contest
