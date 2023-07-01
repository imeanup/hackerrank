class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        if len(digits) == 0:
            return ans

        hm = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        self.backtrack(digits, 0, hm, "", ans)
        return ans

    def backtrack(self, digits: str, i: int, hm: dict, sb: List[str], ans: List[str]):
        if i == len(digits):
            ans.append(sb)
            return
        curr = hm[digits[i]]
        for k in range(len(curr)):
            sb += curr[k]
            self.backtrack(digits, i + 1, hm, sb, ans)
            sb = sb[:-1]
