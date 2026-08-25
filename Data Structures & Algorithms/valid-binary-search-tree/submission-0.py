# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left_bound, right_bound):
            if not node:
                return True
            
            if not left_bound < node.val < right_bound:
                return False

            if not dfs(node.left, left_bound, node.val):
                return False

            return dfs(node.right, node.val, right_bound)

        return dfs(root, float("-inf"), float("inf"))