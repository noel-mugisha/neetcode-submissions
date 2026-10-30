class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for curr_amt in range(coin, amount + 1):
                skip = dp[curr_amt]
                take = dp[curr_amt - coin]

                dp[curr_amt] = skip + take
        
        return dp[-1]