class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def is_pal(l, r):
            count = 0
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            return count
        
        res = 0

        for i in range(0, n):
            res += is_pal(i, i)

            if i < n - 1:
                res += is_pal(i, i + 1)


        return res
        
        