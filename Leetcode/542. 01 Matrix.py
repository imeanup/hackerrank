class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque
        
        m, n = len(mat), len(mat[0])
        dq = deque()
        
        visited = set()
        
        result = [[0]*n for _ in range(m)]
        
        coordinate = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dq.append((i,j))
                    visited.add((i,j))
        
        distance = 0
        while dq:
            for _ in range(len(dq)):
                i, j = dq.popleft()
                if mat[i][j] == 1:
                    result[i][j] = distance
                    
                for c in coordinate:
                    ni = i + c[0]
                    nj = j + c[1]
                    
                    if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                        dq.append((ni, nj))
                        visited.add((ni, nj))
                        
            distance += 1
            
        return result
