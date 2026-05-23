class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for s in strs:
            final_str += str(len(s))
            final_str += '#'
            final_str += s
        return final_str
    def decode(self, s: str) -> List[str]:
        final = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            final.append(s[j+1:j+1+length])
            i = j+1+length
        return final
        