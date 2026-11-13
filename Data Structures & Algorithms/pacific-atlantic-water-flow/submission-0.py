class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = [
            (0, 1), (0, -1), (-1, 0), (1, 0)
        ]

        def bfs(q, visited):
            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if not (0 <= nr < ROWS and 0 <= nc < COLS):
                        continue
                    if heights[nr][nc] < heights[r][c] or (nr, nc) in visited:
                        continue

                    visited.add((nr, nc))
                    q.append((nr, nc))
                
        for r in range(ROWS):
            pacific.add((r, 0))
            atlantic.add((r, COLS - 1))
        for c in range(COLS):
            pacific.add((0, c))
            atlantic.add((ROWS - 1, c))
        
        bfs(deque(pacific), pacific)
        bfs(deque(atlantic), atlantic)

            
        return list(pacific & atlantic)
        