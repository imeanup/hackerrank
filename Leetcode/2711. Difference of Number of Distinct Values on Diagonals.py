class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        answer = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                topLeft = set()
                bottomRight = set()
                for i in range(r):
                    if c - r + i >= 0:
                        topLeft.add(grid[i][c - r + i])
                for i in range(1, min(m - r, n - c)):
                    bottomRight.add(grid[r + i][c + i])
                answer[r][c] = abs(len(topLeft) - len(bottomRight))
        return answer
