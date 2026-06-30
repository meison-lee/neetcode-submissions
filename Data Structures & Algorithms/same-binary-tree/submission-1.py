# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def double_dfs(first, second):
            if (first is None) and (second is None):
                return True
            elif first is None:
                return False
            elif second is None:
                return False

            if first.val != second.val:
                return False

            left_same = double_dfs(first.left, second.left)
            if not left_same:
                return False
            right_same = double_dfs(first.right, second.right)
            if not right_same:
                return False        
            
            return True
        
        return double_dfs(p, q)
            