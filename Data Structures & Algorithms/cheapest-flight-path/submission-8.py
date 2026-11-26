class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        costs = [float("inf")] * n
        for u, v, cost in flights:
            graph[u].append((v, cost))

        costs[src] = 0
        q = deque([(src, 0, -1)])

        while q:
            node, curr_cost, stops = q.popleft()

            for neighbour, cost in graph[node]:
                new_cost = curr_cost + cost
                if new_cost < costs[neighbour] and stops + 1 <= k:
                    costs[neighbour] = new_cost
                    q.append((neighbour, new_cost, stops + 1))

        
        return costs[dst] if costs[dst] != float("inf") else -1