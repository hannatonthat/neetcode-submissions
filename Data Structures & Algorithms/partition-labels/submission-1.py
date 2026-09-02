class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index = {}
        for i, c in enumerate(s):
            index[c] = i
        
        res = []
        curr, end = 0, 0
        for i, c in enumerate(s):
            curr += 1
            end = max(end, index[c])
            if i == end:
                res.append(curr)
                curr = 0
        
        return res