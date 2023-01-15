# https://leetcode.com/contest/weekly-contest-328/problems/count-the-number-of-good-subarrays/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        i = 0; j = 0; n = len(nums); cnt = 0; ans = 0
        mp = {}
        while j<n:
            if nums[j] in mp:
                mp[nums[j]] += 1
            else:
                mp[nums[j]] = 1
            cnt += mp[nums[j]] - 1
            while i < j and cnt >= k:
                ans += n-j
                mp[nums[i]] -= 1
                cnt -= mp[nums[i]]
                i+=1
            j+=1
        return ans
