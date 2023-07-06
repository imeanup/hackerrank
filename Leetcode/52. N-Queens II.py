class Solution:
    def totalNQueens(self, n: int) -> int:
        columns = [False] * n
        rdiag = [False] * (2*n-1)
        ldiag = [False] * (2*n-1)
        ans = 0
        
        def solve(row, columns, rdiag, ldiag):
            nonlocal ans
            if row == n:
                ans += 1
                return
            
            for col in range(n):
                if not columns[col] and not rdiag[row+col] and not ldiag[row-col+n-1]:
                    columns[col] = True
                    rdiag[row+col] = True
                    ldiag[row-col+n-1] = True
                    solve(row+1, columns, rdiag, ldiag)
                    columns[col] = False
                    rdiag[row+col] = False
                    ldiag[row-col+n-1] = False
        
        solve(0, columns, rdiag, ldiag)
        return ans
