class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0

        ROW, COL = len(grid), len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= ROW or col < 0 or col >= COL or grid[row][col] == "0":
                return

            if grid[row][col] == "1":
                grid[row][col] = "0"
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)


        for row in range(0, ROW):
            for col in range(0, COL):
                if grid[row][col] == "1":
                    result += 1
                    dfs(row, col)
        

        return result