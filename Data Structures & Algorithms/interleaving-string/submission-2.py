from functools import lru_cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        x, y, z = len(s1), len(s2), len(s3)
        if x + y != z:
            return False
        

        @lru_cache(None)
        def solve(i, j):
            if i + j >= z:
                return True
            
            if i < x and s1[i] == s3[i + j]:
                if solve(i + 1, j):
                    return True
            
            if j < y and s2[j] == s3[i + j]:
                if solve(i, j + 1):
                    return True
            
            return False

        return solve(0, 0)