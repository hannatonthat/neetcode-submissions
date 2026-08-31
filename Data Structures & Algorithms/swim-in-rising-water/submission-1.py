class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        seen = set()
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        minHeap = []
        heapq.heappush(minHeap, (grid[0][0], 0, 0))
        while minHeap:
            val, x, y = heapq.heappop(minHeap)
            if (x, y) in seen:
                continue
            if x == (n - 1) and y == (n - 1):
                return val
            seen.add((x, y))
            for dr, dc in dirs:
                r, c = x + dr, y + dc
                if (r < 0 or c < 0 or
                    r >= n or c >= n or
                    (r, c) in seen):
                    continue
                heapq.heappush(minHeap, (max(val, grid[r][c]), r, c))