class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left = 0
        right = len(matrix) - 1

        while (left <= right):
            middle = (left + right) // 2
            if target < matrix[middle][0]:
                right = middle - 1
            elif target > matrix[middle][len(matrix[middle]) - 1]:
                left = middle + 1
            else:
                innerLeft = 0
                innerRight = len(matrix[middle]) - 1
                while (innerLeft <= innerRight):
                    innerMiddle = (innerLeft + innerRight) // 2
                    if target < matrix[middle][innerMiddle]:
                        innerRight = innerMiddle - 1
                    elif target > matrix[middle][innerMiddle]:
                        innerLeft = innerMiddle + 1
                    else:
                        return True
                return False

        
        return False