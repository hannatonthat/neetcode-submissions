class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        res = 0

        for n in nums:
            if (n - 1) not in my_set:
                i = 0
                while n + i in my_set:
                    i += 1
                res = max(res, i)
        
        return res