# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            if key in mp:
                mp[key] += [word]
            else:
                mp[key] = [word]
        return (mp.values())
