class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        stack = []
        for s, e in intervals:
            if not stack or stack[-1][1] < s:
                stack.append((s, e))
            else:
                stack[-1] = (min(stack[-1][0], s), max(stack[-1][1], e))
        
        return stack