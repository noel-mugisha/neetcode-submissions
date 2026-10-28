class Solution:
    def rob(self, nums: List[int]) -> int:
        h1 = h2 = 0
        n = len(nums)

        for num in nums:
            h1, h2 = h2, max(h1 + num, h2)

        return max(h1, h2)
        