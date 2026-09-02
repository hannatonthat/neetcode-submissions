class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        my_set = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    my_set.add(i)
        
        return len(my_set) == 3