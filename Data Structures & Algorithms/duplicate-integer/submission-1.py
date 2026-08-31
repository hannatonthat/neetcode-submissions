class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()

        for n in nums:
            if n in my_set:
                return True
            my_set.add(n)
        
        return False