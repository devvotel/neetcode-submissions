class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        seq = 1
        l = 0
        r = 1
        hashS = {s[l]}
        while r < len(s):
            if s[r] not in hashS:
                hashS.add(s[r])
                seq = max(len(hashS), seq)
            else:
                while s[l] != s[r]:
                    hashS.remove(s[l])
                    l+=1
                l+=1
            r+=1
        return seq