class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.components = n

    def find(self, x) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]

        self.components -= 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges, n = [], len(points)

        for i in range(n):
            for j in range(i + 1, n):
                weight = abs(points[i][0]-points[j][0]) + abs(points[i][1] - points[j][1])

                edges.append((i, j, weight))
        
        dsu = DSU(n)
        min_cost = n_edges = 0
        edges.sort(key=lambda x:x[2])

        for u, v, weight in edges:
            if dsu.union(u, v):
                min_cost += weight
                n_edges += 1

                if n_edges == n - 1:
                    return min_cost
        
        return 0
        