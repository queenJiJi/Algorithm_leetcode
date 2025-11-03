class Solution(object):
    def longestValidParentheses(self, s):
        answer = 0
        if not s:
            return answer

        stack = [-1]

        for i in range(len(s)):
            if s[i]== '(':
                stack.append(i)
            else: # s[i] == ')'
                stack.pop()
                if stack: # stack이 비어있지 않다면
                    answer = max(answer, i-stack[-1])
                else: # stack이 비어있다면
                    stack.append(i)
        return answer
                       