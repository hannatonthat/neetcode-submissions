class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n + 1)}
        for u, v, w in times:
            adj[u].append((v, w))
        
        seen = set()
        minHeap = []
        heapq.heappush(minHeap, (0, k)) # time, node
        maxTime = 0

        while minHeap:
            t, u = heapq.heappop(minHeap)
            if u in seen:
                continue
            seen.add(u)
            maxTime = t

            for neighbor, time in adj[u]:
                if neighbor not in seen:
                    heapq.heappush(minHeap, ((t + time, neighbor)))
        
        return maxTime if len(seen) == n else -1