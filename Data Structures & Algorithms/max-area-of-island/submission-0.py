class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        def dfs(grid, i, j, area):
            grid[i][j] = 0
            area+=1
            if (j-1)>=0 and grid[i][j-1] == 1:
                area = dfs(grid, i, j-1, area)
            if (i-1)>=0 and grid[i-1][j] == 1:
                area = dfs(grid, i-1, j, area)
            if (i+1)<len(grid) and grid[i+1][j] == 1:
                area = dfs(grid, i+1, j, area)
            if (j+1)<len(grid[i]) and grid[i][j+1] == 1:
                area = dfs(grid, i, j+1, area)
            return area

        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    area = dfs(grid, i, j, 0)
                    max_area = max(max_area, area)
        return max_area