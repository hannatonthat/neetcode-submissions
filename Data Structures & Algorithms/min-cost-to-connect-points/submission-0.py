class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i:[] for i in range(len(points))}
        for i in range(len(points)):
            xi, yi = points[i]
            for j in range(i + 1, len(points)):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        minHeap = []
        heapq.heappush(minHeap, (0, 0))
        seen = set()
        res = 0

        while minHeap:
            dist, point = heapq.heappop(minHeap)
            if point in seen:
                continue
            seen.add(point)
            res += dist
            for neiDist, nei in adj[point]:
                if nei not in seen:
                    heapq.heappush(minHeap, (neiDist, nei))
        
        return res