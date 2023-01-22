# https://leetcode.com/problems/palindrome-partitioning/description/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def isPalindrome(s):
            l,r = 0, len(s)-1

            while l <= r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        def backtrack(s):
            #print(s, path)
            if not s:
                result.append(list(path))
                return
            

            for i in range(1,len(s)+1):
                if isPalindrome(s[:i]):
                    path.append(s[:i])
                    backtrack(s[i:])
                    path.pop()
        backtrack(s)

        return result
