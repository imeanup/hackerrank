class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chess = [[0 for _ in range(n)] for _ in range(n)]
        columns = [False] * n
        rdiag = [False] * (2*n-1)
        ldiag = [False] * (2*n-1)
        ans = []
        
        def solve(chess, row, columns, rdiag, ldiag, ans):
            if row == len(chess):
                ans.append([''.join(['Q' if chess[i][j] else '.' for j in range(n)]) for i in range(n)])
                return
            
            for col in range(len(chess[0])):
                if not columns[col] and not rdiag[row+col] and not ldiag[row-col+len(chess)-1]:
                    chess[row][col] = True
                    columns[col] = True
                    rdiag[row+col] = True
                    ldiag[row-col+len(chess)-1] = True
                    solve(chess, row+1, columns, rdiag, ldiag, ans)
                    chess[row][col] = False
                    columns[col] = False
                    rdiag[row+col] = False
                    ldiag[row-col+len(chess)-1] = False
        
        solve(chess, 0, columns, rdiag, ldiag, ans)
        return ans

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        chess = [['.' for _ in range(n)] for _ in range(n)]
        self.solve(res, chess, 0, n)
        # print(chess)
        # print(res)
        return res

    def solve(self, res, chess, row, n):
        if row == n:
            res.append([''.join(row) for row in chess])
            return
        for col in range(n):
            if self.isValid(chess, row, col, n):
                chess[row][col] = 'Q'
                self.solve(res, chess, row+1, n)
                chess[row][col] = '.'

    def isValid(self, chess, row, col, n):
        for i in range(row):
            if chess[i][col] == 'Q':
                return False
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if chess[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        k = row - 1
        l = col + 1
        while k >= 0 and l < n:
            if chess[k][l] == 'Q':
                return False
            k -= 1
            l += 1
        return True
