class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        q = deque() # -cnt, time
        t = 0

        while q or maxHeap:
            t += 1
            if not maxHeap:
                t = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append((cnt, t + n))
            if q and q[0][1] == t:
                cnt, time = q.popleft()
                heapq.heappush(maxHeap, cnt)
        
        return t