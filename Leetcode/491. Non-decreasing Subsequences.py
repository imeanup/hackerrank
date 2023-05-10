# https://leetcode.com/problems/non-decreasing-subsequences/description/

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backTracking(start, cur):
            if len(cur) > 1:
                ans.append(cur[:])

            last = cur[-1] if cur else -200
            seen = set()
            
            for i in range(start, n):
                if nums[i] in seen:
                    continue
                if nums[i] >= last:
                    cur.append(nums[i])
                    backTracking(i+1, cur)
                    cur.pop()
                seen.add(nums[i])

        n = len(nums)
        backTracking(0, [])
        return ans
