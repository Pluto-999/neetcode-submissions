class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def search(i, j):
            grid[i][j] = "0"

            left, right, up, down = j - 1, j + 1, i - 1, i + 1

            if left >= 0 and grid[i][left] == "1": search(i, left)
            if right < len(grid[0]) and grid[i][right] == "1": search(i, right)
            if up >= 0 and grid[up][j] == "1": search(up, j)
            if down < len(grid) and grid[down][j] == "1": search(down, j)

        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    result += 1
                    search(i, j)

        return result