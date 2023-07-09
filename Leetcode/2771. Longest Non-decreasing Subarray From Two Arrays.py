class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [[0] * n, [0] * n]
        dp[0][0] = dp[1][0] = 1
        for i in range(1, n):
            for j in range(2):
                dp[j][i] = 1
                if nums1[i] >= nums1[i - 1]:
                    dp[0][i] = max(dp[0][i], dp[0][i - 1] + 1)
                if nums1[i] >= nums2[i - 1]:
                    dp[0][i] = max(dp[0][i], dp[1][i - 1] + 1)
                if nums2[i] >= nums1[i - 1]:
                    dp[1][i] = max(dp[1][i], dp[0][i - 1] + 1)
                if nums2[i] >= nums2[i - 1]:
                    dp[1][i] = max(dp[1][i], dp[1][i - 1] + 1)
        return max(max(dp[0]), max(dp[1]))
