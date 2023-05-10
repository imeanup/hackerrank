'''
https://leetcode.com/problems/substring-with-concatenation-of-all-words/
'''

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: 
            return []
        n, m, k = len(s), len(words), len(words[0])
        
        res = []
        words_map = defaultdict(int)
        
        for word in words:
            words_map[word] += 1
        i, j = 0, 0
        
        while i < n:
            j = i
            words_map_copy = words_map.copy()
            for _ in range(m):
                temp = s[j:j+k]
                if temp in words_map_copy:
                    words_map_copy[temp] -= 1
                    if words_map_copy[temp] == 0:
                        del words_map_copy[temp]
                else:
                    break
                j += k
            if not words_map_copy:
                res.append(i)
            i += 1
        return res

