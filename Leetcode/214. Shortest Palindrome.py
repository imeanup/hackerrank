# https://leetcode.com/problems/shortest-palindrome/

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        lcp = ""
        for i in range(len(s)):
            if s[:i+1] == rev[-i-1:]:
                lcp = s[:i+1]
        return rev[:len(s)-len(lcp)] + s
