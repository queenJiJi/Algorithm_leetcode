class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer= [0] * len(temperatures) 
        stack = []
        for idx,val in enumerate(temperatures):
            while len(stack)!=0 and val> stack[-1][1]:
                item = stack.pop()
                answer[item[0]] = idx- item[0]
            stack.append((idx,val))
        return answer