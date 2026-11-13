class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0)
        ]
        q, fresh = deque(), 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])
        
        time = 0
        while q and fresh > 0:
            len_ = len(q)
            
            for _ in range(len_):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if not (0 <= nr < ROWS and 0 <= nc < COLS):
                        continue
                    if grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2

                        q.append([nr, nc])
            
            time += 1
        
        return time if fresh == 0 else -1
         