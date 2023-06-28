class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
    
    def find(self, root):
        return self.parent[root]
    
    def union(self, root1, root2):
        parX = self.find(root1)
        parY = self.find(root2)
        for i in range(len(self.parent)):
            if self.parent[i] == parX:
                self.parent[i] = parY
    
    def is_connected(self, root1, root2):
        return self.find(root1) == self.find(root2)
