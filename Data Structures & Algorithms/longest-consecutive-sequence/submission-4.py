class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        listSet = set(nums)
        seqs = defaultdict(int)
        for num in nums:
            if (num-1) not in listSet:
                seqs[num]=1

        for key in seqs.keys():
            next = key+1
            while next in listSet:
                seqs[key]+=1
                next+=1
        
        if len(seqs.values()) > 0:
            return max(seqs.values())
        else:
            return 0
