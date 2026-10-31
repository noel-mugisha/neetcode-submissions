from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)

        @lru_cache(None)
        def solve(i, j):
            # We only return true if our p ends and our s also ends, ex: s='a', p='a*b'
            if j >= m:
                return i >= n
            
            first_match = (i < n) and (s[i] == p[j] or p[j] == '.')

            if j + 1 < m and p[j + 1] == '*':
                # We got 2 choices, take or skip it
                take = first_match and solve(i + 1, j)
                skip = solve(i, j + 2)

                return skip or take
            
            return first_match and solve(i + 1, j + 1)
        
        return solve(0, 0)