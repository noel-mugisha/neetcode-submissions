class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def is_pal(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            return l + 1, r - 1
        
        start = max_len = 0

        for i in range(0, n):
            left, right = is_pal(i, i)
            len_ = right - left + 1
            
            if len_ > max_len:
                start, max_len = left, len_

            if i < n - 1:
                left, right = is_pal(i, i + 1)
                len_ = right - left + 1
            
                if len_ > max_len:
                    start, max_len = left, len_


        return s[start : start + max_len]
        