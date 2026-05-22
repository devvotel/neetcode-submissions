class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hsh = defaultdict(int)
        for num in nums:
            hsh[num]+=1
        countarr = [[] for i in range (len(nums)+1)]
        for key, value in hsh.items():
            countarr[value].append(key)

        final = []
        i = len(countarr)-1
        while len(final) < k and i >= 0:
            if (len(countarr) != 0):
                for num in countarr[i]:
                    final.append(num)
                    if len(final) == k:
                        return final
            i -= 1
        return final
