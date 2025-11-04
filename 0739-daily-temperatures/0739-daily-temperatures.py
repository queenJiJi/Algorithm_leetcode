class Solution(object):
    def dailyTemperatures(self, temperatures):
        ans = [0]*len(temperatures)
        stack = []

        for idx,val in enumerate(temperatures):
            while stack and stack[-1][1] < val:
                ans[stack[-1][0]] = idx-stack[-1][0]
                stack.pop()
            stack.append((idx,val))
        return ans
        