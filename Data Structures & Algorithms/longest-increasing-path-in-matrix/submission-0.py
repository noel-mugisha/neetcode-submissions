from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[1] * COLS for _ in range(ROWS)]
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]

        @lru_cache(None)
        def solve(r, c):
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS) and matrix[nr][nc] > matrix[r][c]:
                    dp[r][c] = max(
                        dp[r][c],
                        1 + solve(nr, nc)
                    )

            return dp[r][c]
        
        res = 1

        for r in range(ROWS):
            for c in range(COLS):
                res = max(
                    res,
                    solve(r, c)
                )
        return res