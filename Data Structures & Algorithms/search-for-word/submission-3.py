class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def search(i, j, visited, index):
            
            visited.add((i, j))

            if index == len(word): return True

            result = False

            up, down, left, right = i - 1, i + 1, j - 1, j + 1
            if up >= 0 and board[up][j] == word[index] and (up, j) not in visited:
                result = result or search(up, j, visited, index + 1)
                
            if down < len(board) and board[down][j] == word[index] and (down, j) not in visited:
                result = result or search(down, j, visited, index + 1)
                
            if left >= 0 and board[i][left] == word[index] and (i, left) not in visited:
                result = result or search(i, left, visited, index + 1)
                
            if right < len(board[0]) and board[i][right] == word[index] and (i, right) not in visited:
                result = result or search(i, right, visited, index + 1)
                
            visited.remove((i, j))
            
            return result
            

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if search(i, j, set(), 1): return True

        return False