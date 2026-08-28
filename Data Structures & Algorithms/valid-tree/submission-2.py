class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False

        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]

        self.components -= 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return False

        return True if dsu.components == 1 else False
        