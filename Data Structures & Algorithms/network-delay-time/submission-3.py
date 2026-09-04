class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append((v, t))
        
        minHeap = [[0, k]]
        seen = set()
        t = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in seen:
                continue
            seen.add(node)
            t = time
            for nei, neiTime in adj[node]:
                if nei not in seen:
                    heapq.heappush(minHeap, (neiTime + time, nei))

        return t if len(seen) == n else -1