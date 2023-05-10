# https://leetcode.com/problems/multiply-strings/description/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        pos = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0')) 
                p1, p2 = i + j, i + j + 1
                mul += pos[p2]
                pos[p1] += mul // 10
                pos[p2] = mul % 10
        res = []
        for p in pos:
            if not (len(res) == 0 and p == 0):
                res.append(chr(p + ord('0')))
        return ''.join(res) or "0"
