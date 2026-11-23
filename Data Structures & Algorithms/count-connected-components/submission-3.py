class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {node: [] for node in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set()
        def dfs(node):
            if node in seen:
                return
            
            seen.add(node)

            for neighbor in graph[node]:
                dfs(neighbor)
        
        components = 0
        for node in graph:
            if node not in seen:
                dfs(node)
                components += 1
        
        return components
        