# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        map_ = {val: i for i, val in enumerate(inorder)}
        self.indx = -1

        def helper(start, end):
            if start > end:
                return None

            self.indx += 1
            root = TreeNode(preorder[self.indx])
            
            inorder_indx = map_[root.val]
            
            root.left = helper(start, inorder_indx - 1)
            root.right = helper(inorder_indx + 1, end)

            return root

        return helper(0, len(preorder) - 1)

