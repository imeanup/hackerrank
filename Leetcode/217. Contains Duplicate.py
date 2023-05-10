class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for num in nums:
            if num in mp:
                return True
            else:
                mp[num] = 1
        return False
      
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(list(nums)) == len(set(nums)) else True
      
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(list(nums)) != len(set(nums))
