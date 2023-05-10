class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def window(target):
            i = 0
            j = len(nums) - 1
            res = 0
            
            while i < j:
                if nums[i] + nums[j] > target:
                    j -= 1
                else:
                    res += j - i
                    i += 1
                    
            return res
        
        nums.sort()
        return window(upper) - window(lower-1)
    
