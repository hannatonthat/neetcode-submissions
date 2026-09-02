class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        curr = 0

        l = 0
        for r in range(len(nums)):
            curr += nums[r]
            res = max(res, curr)
            if curr > 0:
                continue
            else:
                l = r
                curr = 0

        return res