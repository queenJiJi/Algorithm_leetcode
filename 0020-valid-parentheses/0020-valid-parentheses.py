class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i=='(':
                stack.append(')')
            elif i == '{':
                stack.append('}')
            elif i== '[':
                stack. append(']')
            elif len(stack)==0 or stack.pop() != i:
                return False
        return True if len(stack)==0 else False