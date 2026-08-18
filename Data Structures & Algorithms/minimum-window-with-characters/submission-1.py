class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = r = 0
        t_dict = Counter(t)
        formed, needed = 0, len(t_dict)
        start, min_len = 0, float("inf")

        for end in range(len(s)):
            c = s[end]
            if c not in t_dict:
                continue
            
            t_dict[c] -= 1
            if t_dict[c] == 0:
                formed += 1
            
            while formed == needed:
                if (end - start + 1) < min_len:
                    min_len = end - start + 1
                    l, r = start, end + 1

                leaving_c = s[start]
                if leaving_c in t_dict:
                    t_dict[leaving_c] += 1
                    if t_dict[leaving_c] > 0:
                        formed -= 1

                start += 1

        return s[l : r]
        