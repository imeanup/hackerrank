class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        def dfs(nums):
            m = len(nums)
            if m < 3:
                return 1
            left = [a for a in nums if a < nums[0]]
            right = [a for a in nums if a > nums[0]]

            lnode = dfs(left)
            rnode = dfs(right)
            combination = comb(m-1, len(left))

            return (lnode * rnode * combination)% MOD

        return (dfs(nums) - 1)% MOD
