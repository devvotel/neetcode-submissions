class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2)
            pair = (dist, point)
            heapq.heappush_max(heap, pair)
            while len(heap) > k:
                heapq.heappop_max(heap)
            
        return [pair[1] for pair in heap]