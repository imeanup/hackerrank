class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        j = 0
        n = len(nums)
        mp = {}
        while j < n:
            if nums[j] in mp:
                mp[nums[j]] += 1
            else:
                mp[nums[j]] = 1
            if j - i + 1 <= k:
                if mp[nums[j]] == 2:
                    return True
            else:
                if len(mp)-1 != k:
                    return True
                mp[nums[i]] -= 1
                if mp[nums[i]] == 0:
                    del mp[nums[i]]
                i += 1
            j += 1
        return False

      
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        j = 0
        n = len(nums)
        mp = set()
        while j < n:
            if nums[j] in mp:
                return True
            mp.add(nums[j])
            if j - i + 1 > k:
                mp.remove(nums[i])
                i += 1

            j += 1
        return False
      
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}

        for i in range(len(nums)):
            if nums[i] in dic and abs(i - dic[nums[i]]) <= k:
                return True
            dic[nums[i]] = i
        return False
