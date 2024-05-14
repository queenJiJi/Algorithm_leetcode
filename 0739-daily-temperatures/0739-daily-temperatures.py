class Solution(object):
    def dailyTemperatures(self, temperatures):
        ans = [0] * len(temperatures)
        stack =[]
        for idx,val in enumerate(temperatures):
            while stack and stack[-1][1] < val:
                prev_day = stack.pop()[0]
                ans[prev_day] = idx-prev_day
            stack.append((idx,val))

        return ans

        