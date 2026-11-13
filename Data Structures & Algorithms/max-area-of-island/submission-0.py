class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0)
        ]

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 0
            if grid[r][c] == 0:
                return 0
            
            area, grid[r][c] = 1, 0

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                area += dfs(nr, nc)
            
            return area
        
        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                max_area = max(max_area, dfs(r, c))

        return max_area

        