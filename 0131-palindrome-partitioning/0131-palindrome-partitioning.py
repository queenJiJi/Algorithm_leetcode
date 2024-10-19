class Solution(object):
    def partition(self, s):
        answer = []
        tmp = []
        def backtrack(start):
            if start == len(s):
                answer.append(tmp[:])
                return

            for i in range(start,len(s)):
                substr = s[start:i+1]
                if substr == substr[::-1]:
                    tmp.append(substr)
                    print(tmp)
                    backtrack(i+1)
                    tmp.pop()

        backtrack(0)
        return answer
   
