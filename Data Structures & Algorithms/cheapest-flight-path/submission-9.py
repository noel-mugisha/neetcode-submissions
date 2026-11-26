from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):

        graph = defaultdict(list)

        for u, v, cost in flights:
            graph[u].append((v, cost))

        costs = [float("inf")] * n
        costs[src] = 0

        q = deque([(src, 0, 0)])

        while q:
            node, curr_cost, stops = q.popleft()

            if stops > k:
                continue

            for neighbor, price in graph[node]:
                new_cost = curr_cost + price

                if new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost

                    q.append((neighbor, new_cost, stops + 1))

        return costs[dst] if costs[dst] != float("inf") else -1