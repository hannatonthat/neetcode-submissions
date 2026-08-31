class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(r, c):
            if (r >= rows or c >= cols
                or r < 0 or c < 0
                or grid[r][c] == 0):
                return 0
            grid[r][c] = 0
            area = 1
            for dr, dc in dirs:
                area += dfs(r + dr, c + dc)
            return area
        
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c))
        return res