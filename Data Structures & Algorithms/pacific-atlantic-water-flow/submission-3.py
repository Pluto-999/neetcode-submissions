class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific_set, atlantic_set = set(), set()
        

        def dfs(i, j, current_set):
            if (i, j) in current_set: return
            current_set.add((i, j))

            up, down, left, right = i - 1, i + 1, j - 1, j + 1

            if up >= 0 and heights[up][j] >= heights[i][j]: 
                dfs(up, j, current_set)
            if down < len(heights) and heights[down][j] >= heights[i][j]:
                dfs(down, j, current_set)
            if left >= 0 and heights[i][left] >= heights[i][j]:
                dfs(i, left, current_set)
            if right < len(heights[0]) and heights[i][right] >= heights[i][j]:
                dfs(i, right, current_set)

        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0: dfs(i, j, pacific_set)
                if i == len(heights) - 1 or j == len(heights[0]) - 1: dfs(i, j, atlantic_set)

        final_set = pacific_set.intersection(atlantic_set)

        result = []

        for (i, j) in final_set:
            result.append([i, j])

        return result