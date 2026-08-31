class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        seen = set()
        
        def addCell(r, c):
            if (r >= rows or c >= cols
                or r < 0 or c < 0
                or grid[r][c] == -1
                or (r, c) in seen):
                return
            seen.add((r, c))
            q.append([r, c])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    seen.add((r, c))
                    q.append([r, c])
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1