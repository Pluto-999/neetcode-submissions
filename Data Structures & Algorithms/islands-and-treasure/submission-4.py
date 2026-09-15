class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        t_location, visited = set(), set()
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0: 
                    t_location.add((i, j))
                    queue.append((i, j))
                    visited.add((i, j))

        counter = 0

        while queue:
            for i in range(len(queue)):
                (i, j) = queue.popleft()

                if counter > 0: grid[i][j] = counter

                up, down, left, right = i - 1, i + 1, j - 1, j + 1

                if up >= 0 and grid[up][j] == 2147483647 and (up, j) not in visited:
                    queue.append((up, j))
                    visited.add((up, j))
                if down < len(grid) and grid[down][j] == 2147483647 and (down, j) not in visited:
                    queue.append((down, j))
                    visited.add((down, j))
                if left >= 0 and grid[i][left] == 2147483647 and (i, left) not in visited:
                    queue.append((i, left))
                    visited.add((i, left))
                if right < len(grid[0]) and grid[i][right] == 2147483647 and (i, right) not in visited:
                    queue.append((i, right))
                    visited.add((i, right))
                

            counter += 1