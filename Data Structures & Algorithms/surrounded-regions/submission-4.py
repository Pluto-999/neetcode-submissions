class Solution:
    def solve(self, board: List[List[str]]) -> None:

        valid_coords = set()

        def search(i, j):
            visited = set()
            visited.add((i, j))
            
            queue = deque()
            queue.append((i, j))
            
            while queue:
                i, j = queue.popleft()
                
                if i - 1 >= 0 and board[i - 1][j] == "O" and (i - 1, j) not in visited:
                    visited.add((i - 1, j))
                    queue.append((i - 1, j))
                if i + 1 < len(board) and board[i + 1][j] == "O" and (i + 1, j) not in visited:
                    visited.add((i + 1, j))
                    queue.append((i + 1, j))
                if j - 1 >= 0 and board[i][j - 1] == "O" and (i, j - 1) not in visited:
                    visited.add((i, j - 1))
                    queue.append((i, j - 1))
                if j + 1 < len(board[0]) and board[i][j + 1] == "O" and (i, j + 1) not in visited:
                    visited.add((i, j + 1))
                    queue.append((i, j + 1))

            valid = True

            for i, j in visited:
                if i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1:
                    valid = False
                    break

            if valid:
                valid_coords.update(visited)


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i, j) not in valid_coords:
                    search(i, j)
                    

        for i, j in valid_coords:
            board[i][j] = "X"
                    
