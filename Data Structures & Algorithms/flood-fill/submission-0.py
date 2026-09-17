class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if image[sr][sc] == color: return image

        visited = set()
        search_color = image[sr][sc]

        def dfs(i, j):
            if image[i][j] == search_color: image[i][j] = color

            up, down, left, right = i - 1, i + 1, j - 1, j + 1
            if up >= 0 and image[up][j] == search_color: dfs(up, j)
            if down < len(image) and image[down][j] == search_color: dfs(down, j)
            if left >= 0 and image[i][left] == search_color: dfs(i, left)
            if right < len(image[0]) and image[i][right] == search_color: dfs(i, right)


        
        dfs(sr, sc)
        return image