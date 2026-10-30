class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        if total_sum < abs(target):
            return 0
        if (total_sum + target) % 2 != 0:
            return 0
        
        target_sum = (total_sum + target) // 2
        dp = [0] * (target_sum + 1)
        dp[0] = 1

        for num in nums:
            for curr_sum in range(target_sum, num - 1, -1):
                skip = dp[curr_sum]
                take = dp[curr_sum - num]

                dp[curr_sum] = skip + take
        
        return dp[-1]

