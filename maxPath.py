"""
Docstring for maxPath

find the max path in a tree
"""

class TreeNode:
    def __init__(self, val=0, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:

    maxSum = float("-inf")
    def maxS(self, root):

        maxSum = float("-inf")


        def dfs(node):

            nonlocal maxSum

            if not node:
                return 0
            
            leftPath = max(dfs(node.left), 0)
            rightPath = max(dfs(node.right), 0)

            currentPath = node.val + leftPath + rightPath

            maxSum = max(maxSum, currentPath)


        dfs(root)

        return maxSum


        

