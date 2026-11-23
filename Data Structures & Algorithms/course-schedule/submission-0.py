from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {node: [] for node in range(numCourses)}
        indegree = {node: 0 for node in range(numCourses)}
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        q = deque([node for node in indegree if indegree[node] == 0])

        ordered = []
        while q:
            q_len = len(q)

            for _ in range(q_len):
                node = q.popleft()

                ordered.append(node)

                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)
        
        return False if len(ordered) != numCourses else True 
        