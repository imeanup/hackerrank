# https://leetcode.com/contest/weekly-contest-332/

class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        p = []
        j = 0
        for i in range(len(s)):
            if j < len(t) and s[i] == t[j]:
                j += 1
            p.append(j)
        ans = len(t) - j
        j = len(t) - 1
        for i in range(len(s)-1, -1, -1):
            ans = min(ans, max(0, j - p[i] + 1))
            if 0 <= j and s[i] == t[j]:
                j -= 1
        return min(ans, j+1)
