class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, a):
            if i == len(nums):
                return 1 if a == target else 0
            if (i, a) in dp:
                return dp[(i, a)]

            dp[(i, a)] = dfs(i + 1, a + nums[i]) + dfs(i + 1, a - nums[i])
            return dp[(i, a)]
        
        return dfs(0, 0)