# https://leetcode.com/contest/biweekly-contest-97/problems/maximum-number-of-integers-to-choose-from-a-range-i/

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        b = [False] * 10005
        s = 0
        ans = 0
        for c in banned:
            b[c] = True
            
        for i in range(1, n+1):
            if not b[i]:
                s += i
                if s > maxSum:
                    break
                ans += 1
        return ans
                
