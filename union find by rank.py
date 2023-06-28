class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, root):
        if root != self.parent[root]:
            self.parent[root] = self.find(self.parent[root])
        return self.parent[root]

    def union(self, root1, root2):
        parX = self.find(root1)
        parY = self.find(root2)
        
        if self.rank[parX] > self.rank[parY]:
            self.parent[parY] = parX
        elif self.rank[parX] < self.rank[parY]:
            self.parent[parX] = parY
        else:
            self.parent[parX] = parY
            self.rank[parY] += 1

    def is_connected(self, root1, root2):
        return self.find(root1) == self.find(root2)
