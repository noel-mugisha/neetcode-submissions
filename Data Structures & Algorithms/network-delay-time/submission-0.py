import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph, INF = {node: [] for node in range(1, n + 1)}, float("inf")
        for u, v, t in times:
            graph[u].append((v, t))

        min_times = {node: INF for node in graph}
        min_times[k] = 0
        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)
            if time > min_times[node]:
                continue
            
            for neighbor, weight in graph[node]:
                new_time = time + weight
                if new_time < min_times[neighbor]:
                    min_times[neighbor] = new_time
                    heapq.heappush(heap, (new_time, neighbor))

        res = max(min_times.values())
        return -1 if res == INF else res
        