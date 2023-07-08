class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if s[j - 1] == '0' and j != i:
                    continue
                if self.pow_five(int(s[j - 1:i], 2)):
                    dp[i] = min(dp[i], dp[j - 1] + 1)

        return dp[n] if dp[n] != float('inf') else -1
    
    def pow_five(self, num):
        while num > 1:
            if num % 5 != 0:
                return False
            num //= 5
        return num == 1
