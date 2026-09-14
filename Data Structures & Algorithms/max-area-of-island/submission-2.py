class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        self.result, self.current = 0, 0

        def search(i, j):
            self.current += 1
            self.result = max(self.result, self.current)
            grid[i][j] = 0

            up, down, left, right = i - 1, i + 1, j - 1, j + 1

            if up >= 0 and grid[up][j] == 1:
                search(up, j)
            if down < len(grid) and grid[down][j] == 1:
                search(down, j)
            if left >= 0 and grid[i][left] == 1:
                search(i, left)
            if right < len(grid[0]) and grid[i][right] == 1:
                search(i, right)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    search(i, j)
                self.current = 0

        return self.result