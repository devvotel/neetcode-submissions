from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sD = defaultdict(int)
        tD = defaultdict(int)
        for c in s:
            sD[c]+=1
        for c in t:
            tD[c]+=1
        if sD == tD:
            return True
        else:
            return False