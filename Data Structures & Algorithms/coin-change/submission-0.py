class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for curr_amt in range(coin, amount + 1):
                skip = dp[curr_amt]
                take = dp[curr_amt - coin] + 1
                
                dp[curr_amt] = min(skip, take)

        return dp[-1] if dp[-1] != float("inf") else -1