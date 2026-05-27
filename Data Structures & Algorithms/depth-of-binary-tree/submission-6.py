# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [(root,1)]
        maxDepth = 0
        while stack:
            cur = stack.pop()
            maxDepth = max(maxDepth, cur[1])
            if cur[0].left:
                newDepth = cur[1] + 1
                stack.append((cur[0].left, newDepth))
            if cur[0].right:
                newDepth = cur[1] + 1
                stack.append((cur[0].right, newDepth))
        return maxDepth