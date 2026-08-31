class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash_map = {}
        for i, c in enumerate(s):
            hash_map[c] = i
        
        size = 0
        end = 0
        res = []
        for i, c in enumerate(s):
            size += 1
            end = max(end, hash_map[c])
            if i == end:
                res.append(size)
                size = 0

        return res