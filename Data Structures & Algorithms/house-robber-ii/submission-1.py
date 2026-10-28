class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob(s, e):
            h1, h2 = 0, 0

            for i in range(s, e + 1):
                h1, h2 = h2, max(nums[i] + h1, h2)

            return max(h1, h2)

        return max(
            rob(0, n - 2),
            rob(1, n - 1)
        )