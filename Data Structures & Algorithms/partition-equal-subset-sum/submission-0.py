class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        my_set = set()
        my_set.add(0)

        for i in range(len(nums) - 1, -1, -1):
            next_set = set()
            for j in my_set:
                next_set.add(j)
                next_set.add(nums[i] + j)
            my_set = next_set
        
        return True if target in my_set else False