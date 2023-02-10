class Solution:
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def maxDistance(self, grid):
        visited = [[grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    q.append((i, j))
        
        distance = -1
        while q:
            q_size = len(q)
            while q_size:
                q_size -= 1
                land_cell = q.popleft()
                for x, y in self.direction:
                    i = land_cell[0] + x
                    j = land_cell[1] + y
                    
                    if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]) and visited[i][j] == 0:
                        visited[i][j] = 1
                        q.append((i, j))
                        
            distance += 1
            
        return distance if distance > 0 else -1
