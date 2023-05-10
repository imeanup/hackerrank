class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(0, 9):
            for j in range(0, 9):
                number = board[i][j]
                if number != ".":
                    if (i, number)  in seen or (number, j)  in seen or (i // 3, j // 3, number)  in seen:
                        return False
                    seen.add((i, number))
                    seen.add((number, j))
                    seen.add((i//3, j//3, number))
        return True
