# https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp = defaultdict(list)
        for i, ch in enumerate(order):
            mp[ch] = i
        print(mp)

        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False
                if words[i][j] != words[i+1][j]:
                    if mp[words[i][j]] > mp[words[i+1][j]]:
                        return False
                    break
        return True
