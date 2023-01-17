# https://leetcode.com/problems/contains-duplicate-iii/description/

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        n = len(nums)
        
        if n == 0 or indexDiff < 0 or valueDiff < 0:
            return False
        
        buckets = {}
        
        for i in range(n):
            if valueDiff == 0:
                bucket = nums[i]
            else:
                bucket = nums[i] // valueDiff
            
            if bucket in buckets:
                return True

            if (bucket - 1) in buckets and abs(nums[i] - buckets[bucket-1]) <= valueDiff:
                return True
            if (bucket + 1) in buckets and abs(buckets[bucket+1] - nums[i]) <= valueDiff:
                return True
            
            buckets[bucket] = nums[i]
            
            if i >= indexDiff:
                if valueDiff == 0:
                    del buckets[nums[i - indexDiff]]
                else:
                    del buckets[nums[i - indexDiff] // valueDiff]
        
        return False
