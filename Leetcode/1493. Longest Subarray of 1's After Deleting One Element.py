class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if sum(nums) == n:
            return n-1
        dp = [[0]*2 for _ in range(n)]
        # print(dp)
        dp[0][0] = nums[0]

        for i in range(1, n):
            if nums[i] == 1:
                dp[i][0] = dp[i-1][0] + 1
                dp[i][1] = dp[i-1][1] + 1
            else:
                dp[i][0] = 0
                dp[i][1] = dp[i-1][0]
        # print(dp)
        return max([i for j in dp for i in j])


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res, l, r = 0, 0, 0
        for i in range(n):
            if nums[i] == 1:
                r += 1
            else:
                l, r = r, 0
            res = max(res, l + r)
        return res if res < n else res - 1


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)

        allones = 0
        onezero = 0
        res = 0
        for n in nums:
            if n == 1:
                allones += 1
                onezero += 1
            else:
                onezero = allones
                allones = 0

            res = max(res, allones, onezero)

        return N - 1 if allones == N else res 
