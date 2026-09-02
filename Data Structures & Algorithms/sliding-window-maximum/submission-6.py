class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        q = deque()
        res = []

        for i in range(k):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])
        l = 0
        for r in range(k, len(nums)):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            l += 1
            if l > q[0]:
                q.popleft()
            res.append(nums[q[0]])
            
        
        return res