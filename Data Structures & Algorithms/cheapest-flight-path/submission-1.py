class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], source: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for src, des, p in flights:
            adj[src].append((p, des))

        minHeap = []
        heapq.heappush(minHeap, (0, source, 0))

        while minHeap:
            price, src, stops = heapq.heappop(minHeap)
            if src == dst:
                return price
            if stops > k:
                continue
            for p, des in adj[src]:
                heapq.heappush(minHeap, (p + price, des, stops + 1))

        return -1