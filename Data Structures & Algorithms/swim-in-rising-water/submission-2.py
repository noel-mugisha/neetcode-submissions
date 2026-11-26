class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set((0, 0))
        heap = [(grid[0][0], 0, 0)]

        while heap:
            time, r, c = heapq.heappop(heap)
            if r == ROWS - 1 and c == COLS - 1:
                return time

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if not (0 <= nr < ROWS and 0 <= nc < COLS):
                    continue
                
                if (nr, nc) not in visited:
                    new_time = max(grid[nr][nc], time)

                    visited.add((nr, nc))
                    heapq.heappush(heap, (new_time, nr, nc))
        