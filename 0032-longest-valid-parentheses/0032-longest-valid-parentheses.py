class Solution(object):
    def longestValidParentheses(self, s):
        # stack =[-1] 
        # answer = 0

        # for i in range(len(s)):
        #     if s[i] =='(':
        #         stack.append(i)
        #     else:
        #         stack.pop()
        #         if stack:
        #             answer = max(answer, i-stack[-1])
        #         else:
        #             stack.append(i)
        # return answer
        stack =[]
        count = 0

        if len(s)==0:
            return count
        
        for ch in s:
            if ch ==')':
                if not stack:
                    continue
                elif stack and stack[-1]==ch:
                    stack.pop()
                    count+=1
            if ch == '(':
                stack.append(')')

        return 2*count