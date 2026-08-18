class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        map_ = defaultdict(int)
        start = 0

        for end in range(len(s)):
            map_[s[end]] += 1

            while (end - start + 1) - max(map_.values()) > k:
                map_[s[start]] -= 1
                start += 1

            longest = max(longest, end - start + 1)

        return longest
        