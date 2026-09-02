class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, subset = [], []
        nums.sort()

        def backtrack(i, curr):
            if curr == target:
                res.append(subset.copy())
                return
            
            for j in range(i, len(nums)):
                if nums[j] + curr > target:
                    return
                subset.append(nums[j])
                backtrack(j, curr + nums[j])
                subset.pop()
            

        backtrack(0, 0)
        return res