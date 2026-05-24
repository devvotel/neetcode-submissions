class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {
            '[':']',
            '(':')',
            '{':'}'
        }
        for c in s:
            if c in matches:
                stack.append(c)
            else:
                if not stack or matches[stack.pop()] != c:
                    return False

        return not stack
