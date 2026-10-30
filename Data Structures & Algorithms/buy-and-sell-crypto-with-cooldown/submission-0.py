from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def solve(can_buy, i):
            if i >= n:
                return 0
            
            res = 0
            if can_buy:
                buy = solve(False, i + 1) - prices[i]
                res = max(res, buy)
            else:
                sell = solve(True, i + 2) + prices[i]
                res = max(res, sell)
            
            cool_down = solve(can_buy, i + 1)
            return max(res, cool_down)
        
        return solve(True, 0)