class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        counts = {}
        start = 0

        for end in range(len(s)):
            counts[s[end]] = counts.get(s[end], 0) + 1

            while (end - start + 1) - max(counts.values()) > k:
                counts[s[start]] -= 1
                start += 1
            
            longest = max(longest, end - start + 1)

        return longest
        