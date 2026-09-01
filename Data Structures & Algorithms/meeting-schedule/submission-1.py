"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        prevEnd = 0
        for i in intervals:
            if i.start < prevEnd:
                return False
            else:
                prevEnd = max(prevEnd, i.end)
        
        return True