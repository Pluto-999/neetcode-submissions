class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        my_set = set()

        def search(row, col, index):
            if index >= len(word):
                return True
            
            if row < 0 or row >= ROW or col < 0 or col >= COL or board[row][col] != word[index] or (row, col) in my_set:
                return False

            my_set.add((row, col))
            result = search(row + 1, col, index + 1) or search(row - 1, col, index + 1) or search(row, col + 1, index + 1) or search(row, col - 1, index + 1)
            my_set.remove((row, col))
            return result

        for row in range(0, ROW):
            for col in range(0, COL):
                if search(row, col, 0):
                    return True

        return False