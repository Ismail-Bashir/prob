"""
word search in using TRIE"""



class TrieNode:

    def __init__():
        self.children = {}
        self.word = None



class Solution:
    def searchWord(self, words, board):


        root = TrieNode()

        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()

                node = node.children[char]
            node.word = word


        res = []
        rows, cols = len(board), len(board[0])

        def dfs(r, c, parent):

            char = board[r][c]

            curr_node = parent.children[char]

            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None

            board[r][c] = "#"

            for dr, dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                dn, cn = r + dr, c + dc

                if 0<=dn<rows and 0<=cn<cols and board[dn][cn] in curr_node.children:
                    dfs(dn,cn, curr_node)


        for r in rows:
            for c in cols:
                if board[r][c] in root.children:
                    dfs(r, c, root.children)



        return res






    

