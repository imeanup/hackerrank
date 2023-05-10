# https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan&id=level-2
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        first = strs[0]
        last = strs[-1]
        print(first, last)
        for i, char in enumerate(first):
            if char != last[i]:
                return first[:i]
        return first
