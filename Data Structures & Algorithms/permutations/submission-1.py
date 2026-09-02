class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        pick = [False] * len(nums)
        res, subset = [], []

        def dfs(pick):
            if len(subset) >= len(nums):
                res.append(subset.copy())
            
            for j in range(len(nums)):
                if not pick[j]:
                    pick[j] = True
                    subset.append(nums[j])
                    dfs(pick)
                    pick[j] = False
                    subset.pop()
        
        dfs(pick)
        return res