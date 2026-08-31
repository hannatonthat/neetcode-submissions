class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0
        def dfs(r, c):
            if (r >= rows or c >= cols
                or r < 0 or c < 0
                or grid[r][c] == "0"):
                return
            grid[r][c] = "0"
            for dr, dc in dirs:
                dfs(r + dr, c + dc)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res