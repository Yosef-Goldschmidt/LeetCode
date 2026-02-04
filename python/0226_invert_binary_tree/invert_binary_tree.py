"""
LeetCode 226: Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
"""
from operator import invert


# ---------- STARTER CODE ----------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


