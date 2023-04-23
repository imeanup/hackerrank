class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if 1 in nums:
            return len(nums) - nums.count(1)
        res = -1
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                d = nums[j]
                for k in range(i, j):
                    d = gcd(d, nums[k])
                if d == 1:
                    if res == -1 or j - i + 1 < res:
                        res = j - i + 1
        if res == -1:
            return -1
        return len(nums) + res - 2
