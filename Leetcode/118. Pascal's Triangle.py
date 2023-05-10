# https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row = [None]*numRows
        for i in range(numRows):
            row[i] = [None]*(i+1)
            row[i][0] = row[i][i] = 1
            for j in range(1, i):
                row[i][j] = row[i-1][j-1]+row[i-1][j]
        return row
