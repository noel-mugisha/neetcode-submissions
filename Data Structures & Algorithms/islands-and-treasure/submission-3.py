class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        island, q = 2147483647, deque()
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
            
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not(0 <= nr < ROWS and 0 <= nc < COLS):
                    continue
                if grid[nr][nc] != island:
                    continue
                
                grid[nr][nc] = grid[r][c] + 1
                q.append([nr, nc])