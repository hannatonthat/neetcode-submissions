class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        self.numFresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    self.numFresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])

        def rot(r, c):
            if (r >= rows or c >= cols
                or r < 0 or c < 0
                or grid[r][c] == 2
                or grid[r][c] == 0):
                return
            q.append([r, c])
            grid[r][c] = 0
            self.numFresh -= 1
        
        time = 0
        while self.numFresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                rot(r + 1, c)
                rot(r - 1, c)
                rot(r, c + 1)
                rot(r, c - 1)
            time += 1
        
        return time if self.numFresh == 0 else -1