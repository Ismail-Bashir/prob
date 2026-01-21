"""
Docstring for minDiff
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:

    def minDiff(self, root:Optional[TreeNode]):

        min_val = float("-inf")
        pre_val = None

        def inorder(node):

            if not node:
                return
            
            inorder(node.left)

            if pre_val is not None:
                min_diff = min(min_diff, node.val-pre_val)

            pre_val = node.val

            inorder(node.right)


        inorder(root)

        return min_diff
