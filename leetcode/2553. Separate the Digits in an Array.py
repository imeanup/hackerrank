# https://leetcode.com/contest/biweekly-contest-97/problems/separate-the-digits-in-an-array/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            ans.extend([int(w) for w in str(num)])
        return ans
