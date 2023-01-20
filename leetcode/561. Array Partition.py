https://leetcode.com/problems/array-partition/description/

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        result = 0
        while left < len(nums):
            result += nums[left]
            left += 2
        return result
