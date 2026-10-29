from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words, n = set(wordDict), len(s)
        min_len, max_len = float("inf"), float("-inf")

        for word in words:
            len_ = len(word)
            min_len, max_len = min(min_len, len_), max(max_len, len_)

        @lru_cache(None)
        def solve(i):
            if i >= n:
                return True
            
            for word_len in range(min_len, max_len + 1):
                if i + word_len <= n and s[i : i + word_len] in words:
                    if solve(i + word_len):
                        return True
            
            return False
        
        return solve(0)
            
