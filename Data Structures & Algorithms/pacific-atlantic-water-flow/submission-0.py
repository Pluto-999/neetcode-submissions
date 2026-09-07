class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROW, COL = len(heights), len(heights[0])
        result = []

        def search(row, col):
            queue = deque()
            queue.append((row, col))
            my_set = set()
            my_set.add((row, col))
            pacific = False
            atlantic = False

            while queue:
                x, y = queue.popleft()
                if x == 0 or y == 0:
                    pacific = True
                if x == ROW - 1 or y == COL - 1:
                    atlantic = True

                # top
                if x - 1 >= 0 and y < COL and heights[x - 1][y] <= heights[x][y] and (x - 1, y) not in my_set:
                    my_set.add((x - 1, y))
                    queue.append((x - 1, y))
                # bottom
                if x + 1 < ROW and y < COL and heights[x + 1][y] <= heights[x][y] and (x + 1, y) not in my_set:
                    my_set.add((x + 1, y))
                    queue.append((x + 1, y))
                # left
                if x < ROW and y - 1 >= 0 and heights[x][y - 1] <= heights[x][y] and (x, y - 1) not in my_set:
                    my_set.add((x, y - 1))
                    queue.append((x, y - 1))
                # right
                if x < ROW and y + 1 < COL and heights[x][y + 1] <= heights[x][y] and (x, y + 1) not in my_set:
                    my_set.add((x, y + 1))
                    queue.append((x, y + 1))

            return pacific and atlantic

        for row in range(0, ROW):
            for col in range(0, COL):
                if search(row, col):
                    result.append([row, col])

        return result