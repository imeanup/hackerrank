# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i = 0
        j = 0
        n = len(s)
        mp = {}
        for c in t:
            mp[c] = mp.get(c, 0) + 1
        print(mp)
        count = len(mp)
        l = 0; r = float('inf')
        while j < n:
            if s[j] in mp:
                mp[s[j]] -= 1
                if mp[s[j]] == 0:
                    count -= 1
            if count == 0:
                while count == 0:
                    if r > j-i+1:
                        r = j-i+1
                        l = i
                    if s[i] in mp:
                        mp[s[i]] += 1
                        if mp[s[i]] > 0:
                            count += 1
                    i += 1
            j += 1
        return "" if r == float('inf') else s[l:r+l]

'''
s = "ADOBECODEBANC"; t = "ABC"
# s = "a"; t = "a"
# s = "a"; t = "aa"
# s = "ab"; t = "a"

c = Solution()
print(c.minWindow(s, t))
'''
