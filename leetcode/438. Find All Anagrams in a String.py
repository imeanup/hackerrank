# Runtime 96ms Beats 98.86%,  Memory 15.2MB Beats 33.55%
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        mp = {}
        for i in p:
            mp[i] = mp.get(i, 0) + 1
        i = j = 0
        ans = []
        count = len(mp)
        n = len(s)
        k = len(p)
        while j < n:
            if s[j] in mp:
                mp[s[j]] -= 1
                if  mp[s[j]] == 0:
                    count -= 1
            if j - i + 1 < k:
                j += 1           
            elif j - i + 1 == k:
                if count == 0:
                    ans.append(i)
                if s[i] in mp:
                    mp[s[i]] += 1
                    if mp[s[i]] == 1:
                        count += 1
                i += 1
                j += 1
        return ans
