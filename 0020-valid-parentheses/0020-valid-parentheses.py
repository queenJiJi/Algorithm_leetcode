class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch =='(':
                stack.append(')')
            elif ch == '{':
                stack.append('}')
            elif ch == '[':
                stack.append(']')
            elif stack and ch == stack[-1]:
                stack.pop()
            else:
                return False
        return False if stack else True