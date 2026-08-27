class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0)
        ]

        dist = 0

        while q:
            size = len(q)
            dist += 1

            for _ in range(size):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < ROWS and 0 <= nc < COLS):
                        continue
                    if (nr, nc) in visited or grid[nr][nc] == -1:
                        continue

                    visited.add((nr, nc))
                    grid[nr][nc] = dist
                    q.append((nr, nc))

                                            
        