class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        q = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        curr = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    newR, newC = r + dr, c + dc
                    if (newR < 0 or newC < 0 or
                        newR >= rows or newC >= cols):
                        continue
                    if grid[newR][newC] == 2147483647:
                        grid[newR][newC] = curr
                        q.append((newR, newC))
            curr += 1
        
        