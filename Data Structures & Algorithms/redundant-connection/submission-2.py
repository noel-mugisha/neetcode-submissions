class DSU:
    def __init__(self, n):
        self.parent = [node for node in range(n + 1)]
        self.size = [1] * (n + 1)
        self.size[0] = 0
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        
        if self.size[root_y] > self.size[root_x]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]

        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        
        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]
        