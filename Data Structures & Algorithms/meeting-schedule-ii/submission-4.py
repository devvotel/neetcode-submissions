"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key = lambda i : i.start)
        count = 1
        occupied = [intervals[0].end]
        for i in range (1, len(intervals)):
            if intervals[i].start >= occupied[0]:
                heapq.heappop(occupied)
            heapq.heappush(occupied, intervals[i].end)
            count = max(count, len(occupied))
        return count
        