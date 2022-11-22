class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        oldColor = image[sr][sc]
        
        self.dfs(sr, sc, image, oldColor, color)
        
        return image
        
    def dfs(self,r, c, image, oldColor, newColor):

        if r < 0 or c < 0 or c >= len(image[0]) or r >= len(image) or image[r][c] != oldColor or image[r][c] == newColor:
            return

        image[r][c] = newColor

        self.dfs(r - 1, c, image, oldColor, newColor)
        self.dfs(r + 1, c, image, oldColor, newColor)
        self.dfs(r, c + 1, image, oldColor, newColor)
        self.dfs(r, c - 1, image, oldColor, newColor)
