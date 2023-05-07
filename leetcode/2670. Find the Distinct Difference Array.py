class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        diff = []
        n = len(nums)
        for i in range(n):
            prefix = len(set(nums[:i+1]))
            suffix = len(set(nums[i+1:]))
            diff.append(prefix-suffix)
        
        return diff
