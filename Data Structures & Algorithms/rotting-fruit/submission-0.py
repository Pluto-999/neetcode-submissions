class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL, result, found_fresh = len(grid), len(grid[0]), -1, False

        queue = deque()

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    found_fresh = True
                if grid[row][col] == 2:
                    queue.append((row, col))

        if not found_fresh:
            return 0
        
        while queue:
            result += 1
            for i in range(len(queue)):
                (x, y) = queue.popleft()

                if x - 1 >= 0 and grid[x - 1][y] == 1:
                    grid[x - 1][y] = 2
                    queue.append((x - 1, y))
                if x + 1 < ROW and grid[x + 1][y] == 1:
                    grid[x + 1][y] = 2
                    queue.append((x + 1, y))
                if y - 1 >= 0 and grid[x][y - 1] == 1:
                    grid[x][y - 1] = 2
                    queue.append((x, y - 1))
                if y + 1 < COL and grid[x][y + 1] == 1:
                    grid[x][y + 1] = 2
                    queue.append((x, y + 1))

        
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    return -1

        
        return result