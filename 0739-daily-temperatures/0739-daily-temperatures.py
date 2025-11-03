class Solution(object):
    def dailyTemperatures(self, temperatures):
        
        record = [0] * len(temperatures)
        stack = [(0,temperatures[0])]

        for idx, val in enumerate(temperatures):
            while stack and stack[-1][1] < val:
                record[stack[-1][0]] = idx - stack[-1][0]
                stack.pop()
            stack.append((idx,val))
        return record