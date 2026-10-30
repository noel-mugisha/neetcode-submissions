from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        @lru_cache(None)
        def solve(i, j):
            if i == m or j == n:
                return 0
            
            if text1[i] == text2[j]:
                return 1 + solve(i + 1, j + 1)
            
            return max(
                solve(i + 1, j),
                solve(i, j + 1)
            )

        return solve(0, 0)