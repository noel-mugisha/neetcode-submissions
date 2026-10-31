from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        @lru_cache(None)
        def solve(i, j):
            if i >= n:
                return m - j
            if j >= m:
                return n - i
            
            if word1[i] == word2[j]:
                return solve(i + 1, j + 1)
            
            return 1 + min(
                solve(i, j + 1), # Insert a char
                solve(i + 1, j), # Del a char
                solve(i + 1, j + 1)
            )

        return solve(0, 0)