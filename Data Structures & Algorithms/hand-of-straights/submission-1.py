class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freqMap = Counter(hand)
        minHeap = list(freqMap.keys())
        heapq.heapify(minHeap)

        while minHeap:
            start = minHeap[0]
            for i in range(start, start + groupSize):
                if i not in freqMap:
                    return False
                freqMap[i] -= 1
                if freqMap[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True