import cProfile

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        ans1 = [0] * n
        ans2 = [0] * m
        tmp = defaultdict(list)
        for i in range(n):
            for j in range(m):
                tmp[mat[i][j]].append((i, j))
        for x in sorted(tmp):
            v1 = Counter()
            v2 = Counter()
            for i, j in tmp[x]:
                v1[i] = max(ans1[i] + 1, ans2[j] + 1, v1[i])
                v2[j] = max(ans1[i] + 1, ans2[j] + 1, v2[j])
            for x in v1:
                ans1[x] = max(ans1[x], v1[x])
            for x in v2:
                ans2[x] = max(ans2[x], v2[x])
        return max(ans1)
      
# solution of the 14th rank
