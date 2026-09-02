class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < len(nums) - 1:
            best = 0
            for i in range(l, r + 1):
                best = max(best, i + nums[i])
            l = r + 1
            r = best
            res += 1
        
        return res