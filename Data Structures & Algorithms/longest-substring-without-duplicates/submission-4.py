class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charSet = set()
        seq = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            seq = max (len(charSet), seq)
        return seq