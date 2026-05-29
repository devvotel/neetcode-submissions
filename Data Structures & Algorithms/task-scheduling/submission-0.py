class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26
        for task in tasks:
            counts[ord(task) - ord('A')]+=1
        
        maxHeap = []
        for i in counts:
            if i > 0:
                maxHeap.append(i)
        
        heapq.heapify_max(maxHeap)
        time = 0
        q = deque() #[count, idleTime]

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop_max(maxHeap) - 1
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush_max(maxHeap,q.popleft()[0])
        
        return time

