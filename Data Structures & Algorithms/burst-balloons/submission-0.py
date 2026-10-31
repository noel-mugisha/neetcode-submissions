class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        coins = [1] + nums + [1]
        n = len(coins)
        dp = [[0] * n for _ in range(n)]

        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap

                for k in range(i + 1, j):
                    gain = coins[i] * coins[k] * coins[j]
                    dp[i][j] = max(
                        dp[i][j],
                        gain + dp[i][k] + dp[k][j]
                    )

        return dp[0][-1]
        