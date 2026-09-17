class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
 
        # checking rows
        for row in range(0, 9):
            row_set = set()
            for col in range(0, 9):
                num = board[row][col]
                if num.isnumeric():
                    if int(num) in row_set: return False
                    else: row_set.add(int(num))

        # checking columns
        for col in range(0, 9):
            col_set = set()
            for row in range(0, 9):
                num = board[row][col]
                if num.isnumeric():
                    if int(num) in col_set: return False
                    else: col_set.add(int(num))

        # checking 3 x 3 sub-boxes
        # need to check: [0][0], [3][0], [6][0]
        #                [0][3], [3][3], [6][3]
        #                [0][6], [3][6], [6][6]

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                sub_box_set = set()
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        num = board[i][j]
                        if num.isnumeric():
                            if int(num) in sub_box_set: return False
                            else: sub_box_set.add(int(num))

        return True