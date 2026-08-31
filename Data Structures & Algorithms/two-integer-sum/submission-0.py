class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, n in enumerate(nums):
            pair = target - n
            if pair in hash_map:
                return [hash_map[pair], i]
            
            hash_map[n] = i