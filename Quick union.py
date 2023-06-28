class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, root):
        while root != self.parent[root]:
            root = self.parent[root]
        return root

    def union(self, root1, root2):
        parX = self.find(root1)
        parY = self.find(root2)
        self.parent[parX] = parY

    def is_connected(self, root1, root2):
        return self.find(root1) == self.find(root2)
