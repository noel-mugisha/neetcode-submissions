from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []

        for num in nums:
            i = bisect_left(res, num)
            if i == len(res):
                res.append(num)
            else:
                res[i] = num

        return len(res)
        