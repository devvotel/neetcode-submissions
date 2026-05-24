class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {
            '[':']',
            '(':')',
            '{':'}'
        }
        for c in s:
            if c == '[' or c == '(' or c == '{':
                stack.append(c)
                print(f"addded {c}")
            else:
                if not stack or matches[stack.pop()] != c:
                    return False

        if not stack:
            return True
        else:
            return False
