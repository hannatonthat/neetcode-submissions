class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >= 2:
            y, x = heapq.heappop(maxHeap), heapq.heappop(maxHeap)
            if x == y:
                continue
            elif x > y:
                heapq.heappush(maxHeap, y - x)
        
        return -maxHeap[0] if maxHeap else 0