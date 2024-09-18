class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                it = board[i][j]
                if it in s:
                    return False
                elif it != '.':
                    s.add(it)

        # Check columns
        for i in range(9):
            s = set()
            for j in range(9):
                it = board[j][i]
                if it in s:
                    return False
                elif it != '.':
                    s.add(it)

        # Check 3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                s = set()
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        it = board[r][c]
                        if it in s:
                            return False
                        elif it != '.':
                            s.add(it)

        return True

        