class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_ = set()
        longest = 0
        start = 0

        for end in range(len(s)):
            while s[end] in set_:
                set_.discard(s[start])
                start += 1

            set_.add(s[end])

            longest = max(longest, end - start + 1)

        return longest

        