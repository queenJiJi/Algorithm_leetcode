class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if s[0] in ']})':
            return False

        for ch in s:
            if ch == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(ch)
            elif ch == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(ch)
            elif ch == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
        
        return False if stack else True