class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        mp = {}
        n = len(nums)
        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1
        dele = max(mp, key=mp.get)
        dcnt = mp[dele]
        lcnt = 0
        
        for i in range(n - 1):
            if nums[i] == dele:
                lcnt += 1
            if lcnt * 2 > i + 1 and (dcnt - lcnt) * 2 > n - i - 1:
                return i
        return -1
    
