class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def eat(k):
            res = 0
            for p in piles:
                res += math.ceil(p / k)
            return res
        
        res = float("inf")
        while l <= r:
            m = (l + r) // 2
            curr = eat(m)
            if curr <= h:
                res = min(res, m)
                    
                r = m - 1
            else:
                l = m + 1
        
        return res