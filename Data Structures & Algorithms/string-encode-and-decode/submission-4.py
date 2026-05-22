class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res = res + str(len(string)) + "#" + string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            delimiter = s.index("#", i)
            length = int(s[i:delimiter])
            print(length)
            print(s[(delimiter+1):(delimiter+1+length)])
            res.append(s[(delimiter+1):(delimiter+1+length)])
            i = delimiter+1+length
        return res
