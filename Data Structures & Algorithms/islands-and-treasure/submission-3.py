class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        queue = deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))

        total = 0
        while queue:
            total += 1
            for i in range(len(queue)):
                (x, y) = queue.popleft()

                # top
                if x - 1 >= 0 and grid[x - 1][y] == 2147483647:
                    grid[x - 1][y] = total
                    queue.append((x - 1, y))

                # bottom
                if x + 1 < len(grid) and grid[x + 1][y] == 2147483647:
                    grid[x + 1][y] = total
                    queue.append((x + 1, y))

                # left
                if y - 1 >= 0 and grid[x][y - 1] == 2147483647:
                    grid[x][y - 1] = total
                    queue.append((x, y - 1))

                # right
                if y + 1 < len(grid[0]) and grid[x][y + 1] == 2147483647:
                    grid[x][y + 1] = total
                    queue.append((x, y + 1))
