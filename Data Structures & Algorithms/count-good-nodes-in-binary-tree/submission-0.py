# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(node, max_path):
            if not node:
                return 
            
            if node.val >= max_path:
                self.count += 1
            
            max_path = max(max_path, node.val)
            dfs(node.left, max_path)
            dfs(node.right, max_path)

        dfs(root, float("-inf"))

        return self.count