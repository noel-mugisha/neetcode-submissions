from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def solve(i):
            if i >= n:
                return 1
            if s[i] == "0":
                return 0

            res = 0
            # let's choose only one number
            res += solve(i + 1)

            if i + 2 <= n and int(s[i : i + 2]) <= 26:
                res += solve(i + 2)

            return res

        return solve(0)      