class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        i = 0
        res = 0
        stack = []
        while i < len(heights):
            start = i
            while stack and stack[-1][0] > heights[i]:
                h, index = stack.pop()
                res = max(res, (h * (i - index)))
                start = index
            stack.append((heights[i], start))
            i += 1
        
        while stack:
            h, index = stack.pop()
            res = max(res, (h * (len(heights) - index)))
        
        return res