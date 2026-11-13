class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0)
        ]

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False
            if grid[r][c] == '0':
                return False
            
            grid[r][c] = '0'

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
            
            return True
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c):
                    res += 1

        return res
        