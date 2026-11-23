class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0)
        ]

        def dfs(r, c):            
            board[r][c] = 'T'
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if not (0 <= nr < ROWS and 0 <= nc < COLS):
                    continue
                
                if board[nr][nc] == 'O':
                    dfs(nr, nc)

        for r in range(ROWS):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][COLS - 1] == 'O':
                dfs(r, COLS - 1)
        
        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[ROWS - 1][c] == 'O':
                dfs(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'X':
                    continue
                
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
                
                else:
                    board[r][c] = 'O'