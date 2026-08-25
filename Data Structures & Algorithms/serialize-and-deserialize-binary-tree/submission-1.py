# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "null"
        
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")

        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "null":
            return None

        nodes = [int(node) if node != "null" else node for node in data.split(",")]

        root = TreeNode(nodes[0])
        indx = 1

        q = deque([root])

        while q:
            node = q.popleft()
            if nodes[indx] != "null":
                node.left = TreeNode(nodes[indx])
                q.append(node.left)

            indx += 1

            if nodes[indx] != "null":
                node.right = TreeNode(nodes[indx])
                q.append(node.right)

            indx += 1

        return root
