"""
Docstring for reveseTree

return tree in reverse
"""

from collections deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:

    def reverseTree(root:Optional[root]):


        if not root:
            return []
        
        result = []

        left_to_right = True
        queue = deque([root])

        while queue:
            level_size = len(queue)
            node = queue.popleft()
            current_level = []

            for _ in range(level_size):

                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)


            if not left_to_right:
                current_level.reverse()

            result.append(current_level)

            left_to_right = not left_to_right

        return result






