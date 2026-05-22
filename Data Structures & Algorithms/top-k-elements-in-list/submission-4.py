class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        freqs = [[] for i in range(len(nums) + 1)]
        for key, value in counts.items():
            freqs[value].append(key)
        res = []
        for arr in reversed(freqs):
            for i in arr:
                res.append(i)
                if len(res) >= k:
                    return res

        return []