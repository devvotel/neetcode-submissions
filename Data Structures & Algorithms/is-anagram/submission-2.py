class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = defaultdict(int)
        for c in s:
            s1[c]+=1
        
        t1 = defaultdict(int)
        for c in t:
            t1[c]+=1
        return s1 == t1