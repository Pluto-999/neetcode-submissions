class Solution:
    def solve(self, board: List[List[str]]) -> None:
        

        ROW, COL = len(board), len(board[0])


        def search(row, col):
            queue = deque()
            queue.append((row, col))
            my_set = set()
            my_set.add((row, col))

            while queue:
                x, y = queue.popleft()
                # then this region does in fact reach a boundary so cannot change it all to O's!
                if x == 0 or x == ROW - 1 or y == 0 or y == COL - 1:
                    queue.clear()
                    my_set.clear()
                    break

                # top
                if x - 1 >= 0 and board[x - 1][y] == "O" and (x - 1, y) not in my_set:
                    my_set.add((x - 1, y))
                    queue.append((x - 1, y))
                # bottom
                if x + 1 < ROW and board[x + 1][y] == "O" and (x + 1, y) not in my_set:
                    my_set.add((x + 1, y))
                    queue.append((x + 1, y))
                # left
                if y - 1 >= 0 and board[x][y - 1] == "O" and (x, y - 1) not in my_set:
                    my_set.add((x, y - 1))
                    queue.append((x, y - 1))
                # right
                if y + 1 < COL and board[x][y + 1] == "O" and (x, y + 1) not in my_set:
                    my_set.add((x, y + 1))
                    queue.append((x, y + 1))


            for x, y in my_set:
                board[x][y] = "X"



        for row in range(0, ROW):
            for col in range(0, COL):
                if board[row][col] == "O" and row != 0 and row != ROW - 1 and col != 0 and col != COL - 1:
                    search(row, col)

