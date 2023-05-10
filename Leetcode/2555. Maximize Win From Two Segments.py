# https://leetcode.com/problems/maximize-win-from-two-segments/description/

class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        prizePositions.sort()
        a = [0] * n
        b = [0] * n
        j = 0
        for i in range(n):
            while j < i and prizePositions[j] + k < prizePositions[i]:
                j += 1
            a[i] = i - j + 1
            if i > 0:
                a[i] = max(a[i], a[i-1])
        j = n - 1
        for i in range(n - 1, -1, -1):
            while j > i and prizePositions[i] + k < prizePositions[j]:
                j -= 1
            b[i] = j - i + 1
            if i + 1 < n:
                b[i] = max(b[i], b[i+1])
        ans = max(a[n-1], b[0])
        for i in range(n - 1):
            ans = max(ans, a[i] + b[i+1])
        return ans
      
  class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        ma = [0] * (n + 1)
        ret = 0
        R = n - 1
        for L in range(n - 1, -1, -1):
            while R >= 0 and prizePositions[L] + k < prizePositions[R]:
                R -= 1
            ma[L] = max(R + 1 - L, ma[L + 1])
            ret = max(ret, R + 1 - L + ma[R + 1])
        return ret
      
  class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)

        pre = [0]*(n+1)
        for i in range(n):
            cur = i + 1 - bisect.bisect_left(prizePositions, prizePositions[i]-k)
            pre[i+1] = pre[i] if pre[i] > cur else cur

        post = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            cur = bisect.bisect_right(prizePositions, prizePositions[i] + k) - i
            post[i] = post[i+1] if post[i+1] > cur else cur
        ans = max(pre[i]+post[i] for i in range(n))
        
        for i in range(n):
            cur = i + 1 - bisect.bisect_left(prizePositions, prizePositions[i]-2*k)
            ans = ans if ans > cur else cur
        return ans
      
class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        r = [0] * (len(prizePositions) + 1)
        p = 0
        res = 0
        curr = 0
        for i in range(len(prizePositions)):
            curr = max(curr, r[i])
            while p < len(prizePositions) and prizePositions[i] + k >= prizePositions[p]:
                p += 1
            c = p - i
            r[p] = max(r[p], c)
            res = max(res, c + curr)

        return res
      
class Solution:
    def maximizeWin(self, a: List[int], k: int) -> int:
        n = len(a)
        dp = [0] * n
        dp2 = [0] * n
        ans = 1
        cur = 0
        for i in range(n):
            while a[i] - a[cur] > k:
                cur += 1
            dp[i] = i - cur + 1
        cur = n - 1
        for i in range(n - 1, -1, -1):
            while a[cur] - a[i] > k:
                cur -= 1
            dp2[i] = cur - i + 1
        mx = dp[0]
        for i in range(1, n):
            ans = max(ans, mx + dp2[i])
            mx = max(mx, dp[i])
        ans = max(ans, mx)
        return ans
      
class Solution:
    def maximizeWin(self, p: List[int], k: int) -> int:
        f = [0] * 100005
        g = [0] * 100005
        lk = 0
        n = len(p)
        ans = 0
        for i in range(n):
            while p[i] - p[lk] > k:
                lk += 1
            if i > 0:
                g[i] = max(g[i-1], i-lk+1)
            else:
                g[i] = i-lk+1
            if lk-1 >= 0:
                f[i] = i-lk+1 + g[lk-1]
            else:
                f[i] = i-lk+1
            ans = max(ans, f[i])
        return ans
      
import heapq

class Solution:
    def maximizeWin(self, p: List[int], k: int) -> int:
        pq = []
        n = len(p)
        dp = [0] * n
        c = 0
        for i in range(n):
            u = p[i]
            while pq and pq[0] < u - k:
                heapq.heappop(pq)
                c -= 1
            heapq.heappush(pq, u)
            c += 1
            dp[i] = max(dp[i-1] if i > 0 else 0, c)
        j = 0
        re = 0
        for i in range(n):
            while j < i and p[j] < p[i] - k:
                j += 1
            re = max(re, i-j+1 + (dp[j-1] if j > 0 else 0))
        return re
      
