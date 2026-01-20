"""
Docstring for board
"""



class Solution:
    def board(self, board: List[List[str]]):

        rows = []
        cols = []
        boards = []


        for _ in range(9):
            rows.append(set())
            cols.append(set())
            boards.append(set())


        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                val  = board[r][c]

                if val in rows[r]:
                    return False
                rows[r].add(val)
                if val in cols[c]:
                    return False
                cols[c].add(val)

                board_idx = (r//3)*3 + (c//3)

                if val in boards[board_idx]:
                    return False
                boards[board_idx].add(val)


        return True