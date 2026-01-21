

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left




class Solution:
    def rightSide(self, root:Optional[TreeNode]):


        result = []



        def dfs(node, depth):

            if not node:
                return 
            
            if len(result) == depth:
                result.append(node.val)


            dfs(node.right,depth+1)
            dfs(node.left, depth+1)


        dfs(root, 0)

        return result