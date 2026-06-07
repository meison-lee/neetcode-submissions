# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True

        def rec(p, q):
            nonlocal res
            if not p and not q:
                return
            if (p and not q) or (q and not p):
                res = False
                return
            if p.val != q.val:
                res = False
                return
            rec(p.left, q.left)
            rec(p.right, q.right)
            return
        
        rec(p, q)
        return res
            