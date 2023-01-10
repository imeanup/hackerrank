# https://leetcode.com/problems/maximum-average-subarray-i/description/
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        i = 0; j = 0
        _max = -float('inf')
        _sum = 0
        while j < n:
            _sum += nums[j]
            if j-i+1 < k:
                j += 1
            elif j-i+1 == k:
                if _max < _sum:
                    _max = _sum
                _sum -= nums[i]
                i += 1
                j += 1
        return _max/k
