class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        q = deque()
        fresh = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        curr = 0
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    newR, newC = r + dr, c + dc
                    if (newR < 0 or newC < 0 or
                        newR >= rows or newC >= cols or
                        grid[newR][newC] != 1):
                        continue
                    grid[newR][newC] = 2
                    q.append((newR, newC))
                    fresh -= 1
            curr += 1

        return curr if fresh == 0 else -1