class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for curr_sum in range(target, num - 1, -1):
                skip = dp[curr_sum]
                take = dp[curr_sum - num]

                dp[curr_sum] = skip or take
        
        return dp[-1]
        