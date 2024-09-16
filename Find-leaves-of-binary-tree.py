from collections import defaultdict
class TreeNode:
    def __init__(self,val, left = None, right= None):
        self.val = val 
        self.left = left
class Solution:
    def find_leaves(root: TreeNode):
        level_map = defaultdict(list)
        def dfs(node, level):
            if not node:
                return level 
            left = dfs(node.left, level)
            right = dfs(node.right, level)
            max_level = max(left, right)
            level_map[max_level].append(node)
            level += 1
        dfs(root, 0)
        return level_map.values()
    def construct_tree(self,li, idx):
        if idx >= len(li):
            return None 
        node = TreeNode(li[idx])
        node.left = self.construct_tree(li,2* idx+1)
        node.right = self.construct_tree(li,2* idx+2)
        return node 

def main():
    li = [1,2,3,4,5,6]
    root = Solution.construct_tree(li)
    result = Solution.find_leaves(root)
    try:
        assert result == [[4, 5, 6], [2, 3], [1]], "Test failed!"  
        print("Test passed!") 
    except AssertionError as e:
        print(e)  




if __name__ == "main":
    main ()



