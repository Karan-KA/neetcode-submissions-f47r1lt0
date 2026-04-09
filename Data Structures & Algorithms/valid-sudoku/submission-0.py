class Solution:
    def isValidSudoku(self, board) -> bool:

        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for i in range(len(board)):
            for j in range(len(board)):

                val = board[i][j]

                if val == '.':
                    continue

                idx = (i//3)*3 + (j//3)
                
                if val in rows[i] or val in columns[j] or val in boxes[idx]:
                    return False

                rows[i].add(val)
                columns[j].add(val)
                boxes[idx].add(val)
        return True