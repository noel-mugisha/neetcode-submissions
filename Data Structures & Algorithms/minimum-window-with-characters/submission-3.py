class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # I'll be needing l and r and will be returning s[l:r]
        # remember r+1
        # I'll be using a hashmap for letter count of t
        # keep track of found and remaining
        l = r = 0
        counts = Counter(t)
        found, required = 0, len(counts)
        start = 0

        for end in range(len(s)):
            c = s[end]
            if c not in counts:
                continue

            counts[c] -= 1
            if counts[c] == 0:
                found += 1

            while found == required:
                start_c = s[start]
                if start_c in counts:
                    counts[start_c] += 1
                    if counts[start_c] > 0:
                        found -= 1
                    
                    if l == r or end - start + 1 < r - l:
                        l, r = start, end + 1
                
                start += 1

        return s[l : r]
        