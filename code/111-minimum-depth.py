# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:  return 0
        if root.left and root.right: return min(1+self.minDepth(root.left),1+self.minDepth(root.right))
        elif root.left: return 1+self.minDepth(root.left)
        elif root.right: return 1+self.minDepth(root.right)
        elif not (root.left or root.right): return 1
