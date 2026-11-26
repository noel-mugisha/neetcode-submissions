class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF, graph = float("inf"), {node: [] for node in range(n)}
        for u, v, weight in flights:
            graph[u].append((v, weight))
        costs = {node: INF for node in graph}
        costs[src] = 0

        q = deque([(0, src, 0)])

        while q:
            cost, node, stops = q.popleft()

            if stops > k:
                continue
            
            for neighbor, weight in graph[node]:
                new_cost = cost + weight
                if new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost

                    q.append((new_cost, neighbor, stops + 1))
        
        return -1 if costs[dst] == INF else costs[dst]
        