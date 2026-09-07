class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        result = 0
        ROW, COL = len(grid), len(grid[0]) 

        def search(row, col):
            if row < 0 or row >= ROW or col < 0 or col >= COL or grid[row][col] == 0:
                return 0

            if grid[row][col] == 1:
                grid[row][col] = 0
                return 1 + search(row + 1, col) + search(row - 1, col) + search(row, col + 1) + search(row, col - 1)



        for row in range(0, ROW):
            for col in range(0, COL):
                if grid[row][col] == 1:
                    result = max(result, search(row, col))

        return result