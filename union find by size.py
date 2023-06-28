class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size

    def find(self, root):
        while root != self.parent[root]:
            root = self.parent[root]
        return root

    def union(self, root1, root2):
        parX = self.find(root1)
        parY = self.find(root2)

        if parX != parY:
            if self.size[parX] < self.size[parY]:
                self.parent[parX] = parY
                self.size[parY] += self.size[parX]
            else:
                self.parent[parY] = parX
                self.size[parX] += self.size[parY]

    def is_connected(self, root1, root2):
        return self.find(root1) == self.find(root2)
