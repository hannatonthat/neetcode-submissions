class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, subset = [], []
        def backtrack(i, curr):
            if curr == target:
                res.append(subset.copy())
                return
            elif i >= len(nums) or nums[i] + curr > target:
                return
            
            subset.append(nums[i])
            backtrack(i + 1, curr + nums[i])
            subset.pop()

            while (i + 1) < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, curr)
        
        backtrack(0, 0)
        return res