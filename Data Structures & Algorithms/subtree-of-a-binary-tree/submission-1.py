# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSameTree (self, p, q):
        if not p and not q:
            return True
        if not (p and q) or (p.val!=q.val):
            return False
        
        return (self.isSameTree(p.left, q.left) and (self.isSameTree(p.right, q.right)))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        elif not root:
            return False
        stack = [root]
        while stack:
            cur = stack.pop()
            if self.isSameTree(cur, subRoot):
                return True
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return False        