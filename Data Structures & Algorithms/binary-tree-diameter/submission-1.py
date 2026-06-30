# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max = 0

        def dfs(node):            
            if node is None:
                return 0
            print("cur:", node.val)

            left = dfs(node.left)
            right = dfs(node.right)
            self.max = max(self.max, left + right)
            print("left, right:", left, right)
            print("max:", self.max)
            if left > right:
                return left + 1
            return right + 1

        dfs(root)
        return self.max