# https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/description/

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        i = 0
        res = 1
        n = len(s)
        while i < n:
            j = i + 1
            while j < n and ord(s[j]) - ord(s[j-1]) == 1:
                j += 1
            res = max(res, j-i)
            i = j
            
        return res
