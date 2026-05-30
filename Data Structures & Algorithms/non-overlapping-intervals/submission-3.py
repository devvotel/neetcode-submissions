class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda i : i[0])
        count = 0
        prev = intervals[0]
        for i in range (1, len(intervals)):
            if intervals[i][0] < prev[1]:
                count += 1
                prev = min(prev, intervals[i], key = lambda i : i[1])
            else:
                prev = intervals[i]
        
        return count