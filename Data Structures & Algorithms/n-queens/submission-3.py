from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        res = []

        def backtrack (row):
            if row == n:
                res.append(["".join(arr) for arr in board])
                return

            for col in range(n):
                if isSafe(row, col):
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'
        
        def isSafe(row, col) -> bool:
            # Check up
            for r in range(row-1, -1, -1):
                if board[r][col] == 'Q':
                    return False
            
            # Check left diagonal
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1
                
            # Check right diagonal
            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c += 1    
            
            return True
        
        backtrack(0)

        return res
