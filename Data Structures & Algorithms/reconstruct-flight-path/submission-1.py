import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for u, v in tickets:
            heapq.heappush(graph[u], v)
        
        res = []

        def dfs(node):
            while graph[node]:
                popped = heapq.heappop(graph[node])
                dfs(popped)
            
            res.append(node)
        
        dfs('JFK')

        return res[::-1]

        
        