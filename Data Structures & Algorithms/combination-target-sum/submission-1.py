class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, subset = [], []

        def backtrack(i, curr):
            if curr == target:
                res.append(subset.copy())
                return
            elif curr > target or i >= len(nums):
                return
            
            subset.append(nums[i])
            backtrack(i, curr + nums[i])
            subset.pop()
            backtrack(i + 1, curr)

        backtrack(0, 0)
        return res