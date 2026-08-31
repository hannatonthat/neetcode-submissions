class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in hash_map:
                return [hash_map[pair], i]
            hash_map[nums[i]] = i
        
        