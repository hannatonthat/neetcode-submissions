class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        def getHours(s):
            res = 0
            for p in piles:
                res += math.ceil(float(p / s))
            return res
        
        while l <= r:
            m = (l + r) // 2
            t = getHours(m)
            if t <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res