class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        
        rowCount = [0] * m
        colCount = [0] * n

        numIndex = {}

        for r in range(m):
            for c in range(n):
                numIndex[mat[r][c]] = (r, c)

        for i, num in enumerate(arr):
            r, c = numIndex[num]
            rowCount[r] += 1
            colCount[c] += 1
            if rowCount[r] == n or colCount[c] == m:
                return i
            
        return -1
