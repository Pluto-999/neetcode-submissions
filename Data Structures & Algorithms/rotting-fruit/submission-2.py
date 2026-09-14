class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))

        result = -1

        while len(queue) > 0:
            result += 1
            for i in range(len(queue)):
                (i, j) = queue.popleft()
                
                
                up, down, left, right = i - 1, i + 1, j - 1, j + 1
                if up >= 0 and grid[up][j] == 1:
                    queue.append((up, j))
                    grid[up][j] = 2
                if down < len(grid) and grid[down][j] == 1:
                    queue.append((down, j))
                    grid[down][j] = 2
                if left >= 0 and grid[i][left] == 1:
                    queue.append((i, left))
                    grid[i][left] = 2
                if right < len(grid[0]) and grid[i][right] == 1:
                    queue.append((i, right))
                    grid[i][right] = 2


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: return -1

        if result == -1: return 0
        return result
