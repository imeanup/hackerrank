class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        n = len(s)
        avail = {}
        for i in range(n):
            if s[i] == '1':
                v = 0
                for j in range(i, min(n, i+30)):
                    v *= 2
                    if s[j] == '1':
                        v += 1
                    if v not in avail:
                        avail[v] = [i, j]
            elif 0 not in avail:
                avail[0] = [i, i]
        ans = []
        for q in queries:
            v = q[0] ^ q[1]
            if v in avail:
                ans.append(avail[v])
            else:
                ans.append([-1, -1])
        return ans
