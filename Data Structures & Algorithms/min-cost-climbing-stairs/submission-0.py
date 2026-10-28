class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c1, c2 = cost[0], cost[1]
        n = len(cost)
        for i in range(2, n):
            c1, c2 = c2, min(c1, c2) + cost[i]

        return min(c1, c2)
        