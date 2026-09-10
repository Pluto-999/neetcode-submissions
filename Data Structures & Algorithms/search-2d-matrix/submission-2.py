class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_length, column_length = len(matrix), len(matrix[0])
        row_left, row_right, column_left, column_right = 0, row_length - 1, 0, column_length - 1

        while row_left <= row_right:
            row_middle = (row_left + row_right) // 2
            row_lowest, row_highest = matrix[row_middle][0], matrix[row_middle][column_right]
            
            # here we have found the row where the target is
            if target >= row_lowest and target <= row_highest:
                while column_left <= column_right:
                    column_middle = (column_left + column_right) // 2
                    
                    if target == matrix[row_middle][column_middle]:
                        return True
                    elif target < matrix[row_middle][column_middle]:
                        column_right = column_middle - 1
                    else:
                        column_left = column_middle + 1

                return False # if not found in this row, then doesn't exist, so stop looping and return False

            # the lowest value in this row is too high when compared to the target !
            elif target < row_lowest: row_right = row_middle - 1

            # the highest value in this row is too low when compared to the target !
            else: row_left = row_middle + 1
        
        return False